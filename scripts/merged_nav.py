import json
import yaml
import os

# Top-level title of the nav section merged in from the openapi repo.
OPENAPI_TITLE = 'OpenAPI 文档'
# The merged section is inserted right before this top-level title.
INSERT_BEFORE_TITLE = '下载中心'


def merged_nav(master_nav,openapi_nav):
    # Check file 
    if os.path.exists(master_nav) and os.path.exists(openapi_nav):
        # Load the master_nav YAML file
        with open(master_nav, encoding='utf-8') as f:
            master = yaml.load(f, Loader=yaml.FullLoader)

        # Load the openapi YAML file
        with open(openapi_nav, encoding='utf-8') as f:
            openapi = yaml.load(f, Loader=yaml.FullLoader)

        json_master = json.dumps(master, ensure_ascii=False)
        json_openapi = json.dumps(openapi, ensure_ascii=False)

        master_nav_items = json.loads(json_master)['nav']
        openapi_nav_items = json.loads(json_openapi)['nav']

        # Idempotency: drop a previously merged OpenAPI section so that
        # re-running this script on an already merged nav does not duplicate it.
        master_nav_items = [
            item for item in master_nav_items
            if not (isinstance(item, dict) and OPENAPI_TITLE in item)
        ]

        # Insert the OpenAPI section right before the "下载中心" top-level item
        # so the tabs read: 首页 / 产品文档 / OpenAPI 文档 / 下载中心 / ...
        insert_pos = len(master_nav_items)
        for i, item in enumerate(master_nav_items):
            if isinstance(item, dict) and INSERT_BEFORE_TITLE in item:
                insert_pos = i
                break

        merged_nav = (
            master_nav_items[:insert_pos]
            + openapi_nav_items
            + master_nav_items[insert_pos:]
        )

        # Convert merged_nav to YAML and save to disk
        with open('docs/zh/navigation.yml', 'w', encoding='utf-8') as f:
            yaml.dump({'nav': merged_nav}, f, allow_unicode=True)
    else:
        print('One or both of the files do not exist.')


if __name__ == '__main__':
    merged_nav('docs/zh/navigation.yml', 'dao-openapi/openapi-nav.yml')
