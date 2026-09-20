import os
import yaml

# The d.run section must sit right after "DaoCloud Enterprise", matching the
# "Product Docs" dropdown grouping in docs/en/theme/partials/tabs.html.
# Note: do not anchor on something like "Videos" as its top-level position
# shifts; use a stable anchor so the drawer nav follows the real nav order.
ANCHOR_TITLE = "DaoCloud Enterprise"
TF_TITLE = "d.run Token Factory"


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