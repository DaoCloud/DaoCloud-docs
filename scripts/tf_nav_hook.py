import os
import yaml

# d.run 条目固定在「DaoCloud Enterprise」之后，和 docs/zh/theme/partials/tabs.html
# 里「产品文档」下拉的分组保持一致。
# 注意：不要用「视频教程」之类的条目做锚点，否则 d.run 条目会跟着无关条目的
# 位置漂移（抽屉导航 md-nav--primary 会按真实 nav 顺序渲染这些顶层条目）。
ANCHOR_TITLE = "DaoCloud Enterprise"
TF_TITLE = "d.run Token 工厂效能平台"


def on_config(config):
    tf_nav_path = os.path.join(os.path.dirname(config["docs_dir"]), "tf.yml")

    if not os.path.exists(tf_nav_path):
        return config

    with open(tf_nav_path, "r", encoding="utf-8") as f:
        tf_data = yaml.safe_load(f)

    tf_items = tf_data.get("nav", [])
    if not tf_items:
        return config

    nav = list(config["nav"])

    nav = [
        item
        for item in nav
        if not (isinstance(item, dict) and TF_TITLE in item)
    ]

    insert_pos = len(nav)
    for i, item in enumerate(nav):
        if isinstance(item, dict) and ANCHOR_TITLE in item:
            insert_pos = i + 1
            break

    for item in reversed(tf_items):
        nav.insert(insert_pos, item)

    config["nav"] = nav
    return config
