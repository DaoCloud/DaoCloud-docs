import os
import yaml


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
        if not (isinstance(item, dict) and "Token 工厂 文档" in item)
    ]

    insert_pos = len(nav)
    for i, item in enumerate(nav):
        if isinstance(item, dict) and "视频教程" in item:
            insert_pos = i
            break

    for item in reversed(tf_items):
        nav.insert(insert_pos, item)

    config["nav"] = nav
    return config
