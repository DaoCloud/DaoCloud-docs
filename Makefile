COMMAND := $(firstword $(MAKECMDGOALS))
REQUESTED_LANG := $(word 2,$(MAKECMDGOALS))
ifeq ($(REQUESTED_LANG),)
ifneq ($(filter build build-path,$(COMMAND)),)
LANG := all
else
LANG := zh
endif
else
LANG := $(REQUESTED_LANG)
endif
LANGS := zh en
BUILD_TARGETS := zh en all
DOCS_PATH ?= docs/zh/docs
LSYNC_PATH ?= docs/en
FILE ?=
FOLDER ?=
PDF ?=
OUT ?=

BOLD  := \033[1m
CYAN  := \033[36m
GREEN := \033[32m
RED   := \033[31m
RESET := \033[0m

.DEFAULT_GOAL := help

ifneq ($(filter serve,$(MAKECMDGOALS)),)
ifneq ($(filter all,$(MAKECMDGOALS)),)
$(error Usage: make serve [zh|en])
endif
endif

# -- Setup -------------------------------------------------------------------

sync: ## Install default dependencies with uv
	@printf '\n$(BOLD)Syncing default dependencies$(RESET)\n'
	uv sync --locked --no-install-project
	@printf '\n$(GREEN)OK dependencies synced$(RESET)\n\n'

sync-upload: ## Install upload dependencies with uv
	@printf '\n$(BOLD)Syncing upload dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group upload
	@printf '\n$(GREEN)OK upload dependencies synced$(RESET)\n\n'

sync-link-check: ## Install link-check dependencies with uv
	@printf '\n$(BOLD)Syncing link-check dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group link-check
	@printf '\n$(GREEN)OK link-check dependencies synced$(RESET)\n\n'

sync-pdf: ## Install Word/PDF dependencies with uv
	@printf '\n$(BOLD)Syncing Word/PDF dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group pdf
	@printf '\n$(GREEN)OK Word/PDF dependencies synced$(RESET)\n\n'

sync-pdf-tools: ## Install PDF utility dependencies with uv
	@printf '\n$(BOLD)Syncing PDF utility dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group pdf-tools
	@printf '\n$(GREEN)OK PDF utility dependencies synced$(RESET)\n\n'

sync-translate: ## Install translation dependencies with uv
	@printf '\n$(BOLD)Syncing translation dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group translate
	@printf '\n$(GREEN)OK translation dependencies synced$(RESET)\n\n'

sync-report: ## Install report dependencies with uv
	@printf '\n$(BOLD)Syncing report dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group report
	@printf '\n$(GREEN)OK report dependencies synced$(RESET)\n\n'

sync-image: ## Install image utility dependencies with uv
	@printf '\n$(BOLD)Syncing image utility dependencies$(RESET)\n'
	uv sync --locked --no-install-project --group image
	@printf '\n$(GREEN)OK image utility dependencies synced$(RESET)\n\n'

# -- Docs --------------------------------------------------------------------

serve: ## Preview docs locally with uv, defaults to zh
	@if [ "$(LANG)" = "all" ]; then \
		printf '$(RED)Usage: make serve [zh|en]$(RESET)\n'; \
		exit 2; \
	fi
	@if ! echo "$(LANGS)" | grep -qw "$(LANG)"; then \
		printf '$(RED)Usage: make serve [zh|en]$(RESET)\n'; \
		exit 2; \
	fi
	@printf '\n$(BOLD)Serving $(LANG) docs$(RESET)\n'
	@printf '  $(CYAN)uv run mkdocs serve -f docs/$(LANG)/mkdocs.yml$(RESET)\n\n'
	uv run mkdocs serve -f docs/$(LANG)/mkdocs.yml

build: ## Build docs with uv, defaults to all
	@if ! echo "$(BUILD_TARGETS)" | grep -qw "$(LANG)"; then \
		printf '$(RED)Usage: make build [zh|en|all]$(RESET)\n'; \
		exit 2; \
	fi
	@set -e; \
	if [ "$(LANG)" = "all" ]; then \
		printf '\n$(BOLD)[1/2] Building zh docs$(RESET)\n'; \
		uv run mkdocs build -f docs/zh/mkdocs.yml -d ../../public/; \
		printf '\n$(BOLD)[2/2] Building en docs$(RESET)\n'; \
		uv run mkdocs build -f docs/en/mkdocs.yml -d ../../public/en/; \
	elif [ "$(LANG)" = "zh" ]; then \
		printf '\n$(BOLD)Building zh docs$(RESET)\n'; \
		uv run mkdocs build -f docs/zh/mkdocs.yml -d ../../public/; \
	else \
		printf '\n$(BOLD)Building en docs$(RESET)\n'; \
		uv run mkdocs build -f docs/en/mkdocs.yml -d ../../public/en/; \
	fi
	@printf '\n$(GREEN)OK docs build complete$(RESET)\n\n'

build-path: ## Build path-based docs with uv, defaults to all
	@if ! echo "$(BUILD_TARGETS)" | grep -qw "$(LANG)"; then \
		printf '$(RED)Usage: make build-path [zh|en|all]$(RESET)\n'; \
		exit 2; \
	fi
	@set -e; \
	if [ "$(LANG)" = "all" ]; then \
		printf '\n$(BOLD)[1/2] Building zh path docs$(RESET)\n'; \
		uv run mkdocs build -f docs/zh/mkdocs.path.yaml -d ../../public/; \
		printf '\n$(BOLD)[2/2] Building en path docs$(RESET)\n'; \
		uv run mkdocs build -f docs/en/mkdocs.path.yaml -d ../../public/en/; \
	elif [ "$(LANG)" = "zh" ]; then \
		printf '\n$(BOLD)Building zh path docs$(RESET)\n'; \
		uv run mkdocs build -f docs/zh/mkdocs.path.yaml -d ../../public/; \
	else \
		printf '\n$(BOLD)Building en path docs$(RESET)\n'; \
		uv run mkdocs build -f docs/en/mkdocs.path.yaml -d ../../public/en/; \
	fi
	@printf '\n$(GREEN)OK path docs build complete$(RESET)\n\n'

generate-nav: ## Generate preview navigation
	@printf '\n$(BOLD)Generating navigation$(RESET)\n'
	uv run python scripts/generate_nav.py
	@printf '\n$(GREEN)OK navigation generated$(RESET)\n\n'

netlify-preview: ## Build Netlify preview output
	@printf '\n$(BOLD)Building Netlify preview$(RESET)\n'
	bash scripts/run_netlify.sh

docx: ## Generate Word document, override DOCS_PATH=docs/zh/docs
	@printf '\n$(BOLD)Generating Word document from $(DOCS_PATH)$(RESET)\n'
	uv run --group pdf python scripts/md2doc-v2.py "$(DOCS_PATH)"
	@printf '\n$(GREEN)OK Word document generated$(RESET)\n\n'

word-count: ## Count Markdown characters in the repository
	@printf '\n$(BOLD)Counting Markdown characters$(RESET)\n'
	uv run python scripts/word_count.py

lsync: ## Check localized docs sync, override LSYNC_PATH=docs/en
	@printf '\n$(BOLD)Checking localized docs sync for $(LSYNC_PATH)$(RESET)\n'
	bash scripts/lsync.sh "$(LSYNC_PATH)"

# -- Translation --------------------------------------------------------------

translate-file: ## Translate one Markdown file, FILE=path/to/file.md
	@if [ -z "$(FILE)" ]; then \
		printf '$(RED)Usage: make translate-file FILE=path/to/file.md$(RESET)\n'; \
		exit 2; \
	fi
	@printf '\n$(BOLD)Translating $(FILE)$(RESET)\n'
	uv run --group translate python scripts/translate_md.py --file "$(FILE)"

translate-folder: ## Translate Markdown files in a folder, FOLDER=path/to/folder
	@if [ -z "$(FOLDER)" ]; then \
		printf '$(RED)Usage: make translate-folder FOLDER=path/to/folder$(RESET)\n'; \
		exit 2; \
	fi
	@printf '\n$(BOLD)Translating folder $(FOLDER)$(RESET)\n'
	uv run --group translate python scripts/translate_md.py --folder "$(FOLDER)"

translate-all: ## Translate all Chinese docs into English
	@printf '\n$(BOLD)Translating all Chinese docs$(RESET)\n'
	cd docs/zh && uv run --group translate python ../../scripts/translate_md.py --full_translate True

# -- Images ------------------------------------------------------------------

upload-images: ## Upload local images referenced by docs, override DOCS_PATH=docs
	@printf '\n$(BOLD)Uploading images referenced under $(DOCS_PATH)$(RESET)\n'
	uv run --group image python scripts/upload_img_ucloud.py "$(DOCS_PATH)"

upload-md-images: ## Upload local images referenced by one Markdown file, FILE=path/to/file.md
	@if [ -z "$(FILE)" ]; then \
		printf '$(RED)Usage: make upload-md-images FILE=path/to/file.md$(RESET)\n'; \
		exit 2; \
	fi
	@printf '\n$(BOLD)Uploading images referenced by $(FILE)$(RESET)\n'
	uv run --group image python scripts/md_image_analyzer.py "$(FILE)"

# -- PDF ---------------------------------------------------------------------

pdf-unlock: ## Remove PDF encryption, PDF=input.pdf optional OUT=output.pdf
	@if [ -z "$(PDF)" ]; then \
		printf '$(RED)Usage: make pdf-unlock PDF=input.pdf [OUT=output.pdf]$(RESET)\n'; \
		exit 2; \
	fi
	@printf '\n$(BOLD)Removing PDF encryption from $(PDF)$(RESET)\n'
	@if [ -z "$(OUT)" ]; then \
		uv run --group pdf-tools python scripts/remove_pdf_password.py "$(PDF)"; \
	else \
		uv run --group pdf-tools python scripts/remove_pdf_password.py "$(PDF)" "$(OUT)"; \
	fi

pdf: ## Build PDF with docs/zh/pdf.yaml
	@printf '\n$(BOLD)Building PDF docs$(RESET)\n'
	uv run --group pdf mkdocs build -f docs/zh/pdf.yaml
	@printf '\n$(GREEN)OK PDF docs build complete$(RESET)\n\n'

# -- External content --------------------------------------------------------

merge-openapi-docs: ## Merge OpenAPI docs into Chinese docs
	@printf '\n$(BOLD)Merging OpenAPI docs$(RESET)\n'
	cp -av dao-openapi/docs/openapi docs/zh/docs/
	uv run python scripts/merged_nav.py
	@printf '\n$(GREEN)OK OpenAPI docs merged$(RESET)\n\n'

merge-download-docs: ## Merge download docs into Chinese and English docs
	@printf '\n$(BOLD)Merging download docs$(RESET)\n'
	cp -av daocloud-download-docs/docs/zh/docs/download docs/zh/docs/
	cp -av daocloud-download-docs/docs/en/docs/download docs/en/docs/
	@printf '\n$(GREEN)OK download docs merged$(RESET)\n\n'

merge-external-docs: ## Merge all checked-out external docs
	@$(MAKE) --no-print-directory merge-openapi-docs
	@$(MAKE) --no-print-directory merge-download-docs

# -- CI ----------------------------------------------------------------------

check-links: ## Check compatibility links and write check-results.txt
	@printf '\n$(BOLD)Checking compatibility links$(RESET)\n'
	uv run --group link-check python scripts/check_links.py > check-results.txt
	@printf '$(GREEN)OK wrote check-results.txt$(RESET)\n\n'

release-notes: ## Sync project release notes from GitHub releases
	@printf '\n$(BOLD)Syncing project release notes$(RESET)\n'
	bash scripts/release.sh

# -- Deploy ------------------------------------------------------------------

upload-ucloud: ## Upload public directory to UCloud
	@printf '\n$(BOLD)Uploading public directory to UCloud$(RESET)\n'
	cd public && uv run --group upload python ../scripts/upload-ucloud.py public_key=$$UCLOUD_PUBLICKEY private_key=$$UCLOUD_PRIVATEKEY region=$$UCLOUD_REGION bucket=$$UCLOUD_BUCKET
	@printf '\n$(GREEN)OK UCloud upload complete$(RESET)\n\n'

refresh-cdn-cache: ## Refresh UCloud CDN cache
	@printf '\n$(BOLD)Refreshing CDN cache$(RESET)\n'
	uv run --group upload python scripts/refresh_cdn_cache.py publickey=$$UCLOUD_PUBLICKEY privatekey=$$UCLOUD_PRIVATEKEY
	@printf '\n$(GREEN)OK CDN cache refresh complete$(RESET)\n\n'

# -- Docker ------------------------------------------------------------------

serve-docker: ## Preview Chinese docs with Docker
	@printf '\n$(BOLD)Serving zh docs with Docker$(RESET)\n'
	@printf '  $(CYAN)http://localhost:8000$(RESET)\n\n'
	docker run --rm -it -e ENABLED_GIT_REVISION_DATE="false" -p 8000:8000 -v ${PWD}/docs/zh:/docs squidfunk/mkdocs-material

# -- Maintenance -------------------------------------------------------------

clean: ## Remove generated site files
	@printf '\n$(BOLD)Removing generated site files$(RESET)\n'
	rm -rf public site docs/zh/site docs/en/site
	@printf '$(GREEN)OK clean complete$(RESET)\n\n'

# -- Help --------------------------------------------------------------------

help: ## Show available targets
	@awk 'BEGIN {FS = ":.*## "; printf "\n$(BOLD)DaoCloud-docs$(RESET) - docs tooling\n\n$(BOLD)Usage$(RESET)\n  $(CYAN)make [target] [zh|en|all]$(RESET)\n"} \
		/^# -- / {n = $$0; gsub(/(^# -- | -+$$)/, "", n); printf "\n$(BOLD)%s$(RESET)\n", n} \
		/^[a-zA-Z_-]+:.*## / {printf "  $(CYAN)make %-22s$(RESET) %s\n", $$1, $$2} \
		END {printf "\n"}' $(MAKEFILE_LIST)

zh en all:
	@:

.PHONY: clean serve build build-path sync sync-upload sync-link-check sync-pdf sync-pdf-tools sync-translate sync-report sync-image generate-nav netlify-preview docx word-count lsync translate-file translate-folder translate-all upload-images upload-md-images pdf-unlock pdf merge-openapi-docs merge-download-docs merge-external-docs check-links release-notes upload-ucloud refresh-cdn-cache serve-docker help zh en all
