#!/usr/bin/env python3
"""Validate the redirect_maps of every MkDocs config in this repository.

mkdocs-redirects silently ignores a rule when its target page cannot be found in
the file tree: it only logs a warning and skips the rule, so no redirect HTML is
written and the old URL keeps returning 404. This has actually happened here --
the English configs carried a bogus "en/" path prefix while docs_dir is
docs/en/docs, which made all 25 English redirects no-ops.

This script turns those silent warnings into a hard failure so the mistake cannot
be merged again.

Checks per rule:
  ERROR   the key is not a markdown file (e.g. a trailing slash) - the rule can
          never produce the intended page
  ERROR   the target does not exist in the file tree and is not an external URL
  WARNING the old path still exists as a real page, so the generated redirect
          HTML will overwrite it (normally the old file should be removed)

Exit code is 1 when at least one ERROR is found.
"""

import glob
import os
import sys

from mkdocs.config import load_config
from mkdocs.structure.files import get_files


def discover_configs():
    """Return every lang config that declares a redirects plugin."""
    found = []
    for pattern in ("docs/*/mkdocs*.yml", "docs/*/mkdocs*.yaml"):
        for path in sorted(glob.glob(pattern)):
            try:
                with open(path, encoding="utf-8") as f:
                    content = f.read()
            except OSError:
                continue
            if "redirect_maps" in content:
                found.append(path)
    return found


def check_config(path):
    """Return (errors, warnings, rule_count) for one config file."""
    errors = []
    warnings = []

    try:
        cfg = load_config(path)
        files = get_files(cfg)
        plugin = cfg["plugins"]["redirects"]
        plugin.on_files(files, cfg)
    except Exception as exc:  # noqa: BLE001 - surface any config failure as an error
        return [f"cannot load config: {exc}"], warnings, 0

    doc_pages = plugin.doc_pages
    docs_dir = cfg["docs_dir"]

    for page_old, page_new in plugin.redirects.items():
        page_new = "" if page_new is None else str(page_new)
        target, _, _fragment = page_new.partition("#")

        if not page_old.endswith(".md"):
            errors.append(f"'{page_old}' is not a valid markdown file")
            continue

        if page_new.lower().startswith(("http://", "https://")):
            continue

        if target not in doc_pages:
            errors.append(
                f"redirect target '{page_new}' does not exist "
                f"(expected {os.path.join(docs_dir, target)})"
            )
            continue

        if os.path.isfile(os.path.join(docs_dir, page_old)):
            warnings.append(
                f"'{page_old}' still exists as a real page, so the redirect HTML "
                f"will overwrite it (target: {page_new})"
            )

    return errors, warnings, len(plugin.redirects)


def main():
    configs = discover_configs()
    if not configs:
        print("No config with redirect_maps found.")
        return 0

    total_errors = 0
    for path in configs:
        errors, warnings, rules = check_config(path)
        status = "FAIL" if errors else "OK"
        print(f"[{status}] {path} ({rules} rule(s))")
        for warning in warnings:
            print(f"       WARNING  {warning}")
        for error in errors:
            print(f"       ERROR    {error}")
        total_errors += len(errors)

    print()
    if total_errors:
        print(
            f"FOUND {total_errors} problem(s) in redirect_maps. "
            "Redirect keys and targets are relative to each config's docs_dir "
            "(e.g. docs/en/docs for docs/en/mkdocs.yml), so do not prefix them "
            "with the language folder."
        )
        return 1

    print("OK all redirect maps are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
