import os
import yaml


def on_config(config):
    drun_nav_path = os.path.join(os.path.dirname(config["docs_dir"]), "drun.yml")

    if not os.path.exists(drun_nav_path):
        return config

    with open(drun_nav_path, "r", encoding="utf-8") as f:
        drun_data = yaml.safe_load(f)

    drun_items = drun_data.get("nav", [])
    if not drun_items:
        return config

    nav = list(config["nav"])

    nav = [
        item
        for item in nav
        if not (isinstance(item, dict) and "d.run 文档" in item)
    ]

    insert_pos = len(nav)
    for i, item in enumerate(nav):
        if isinstance(item, dict) and "Token 工厂文档" in item:
            insert_pos = i + 1
            break

    for item in reversed(drun_items):
        nav.insert(insert_pos, item)

    config["nav"] = nav
    return config
