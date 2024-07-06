# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""

import json
import os
from typing import TypedDict, Any, Union, List

import yaml

# MODULES read from scripts/models.json
with open('scripts/dce_models.json', 'r') as f:
    MODULES = json.load(f)


class ModuleDict(TypedDict):
    module_name: Any


def extract_module_from_yaml(yaml_file_path: str, module_name: str) -> Union[ModuleDict, None]:
    def search(item: ModuleDict, path: List[str]) -> Union[ModuleDict, None]:
        for key, value in item.items():
            if key == module_name:
                return {key: value}
            elif isinstance(value, dict):
                result = search(value, path + [key])
                if result:
                    return {key: result}
            elif isinstance(value, list):
                for sub_item in value:
                    if isinstance(sub_item, dict):
                        result = search(sub_item, path + [key])
                        if result:
                            return {key: [result]}
        return None
    
    # Read the YAML file
    with open(yaml_file_path, 'r', encoding='utf-8') as file:
        yaml_data = yaml.safe_load(file)
    
    # Extract the module
    extracted = search(yaml_data, []) or {}
    
    # Convert the extracted module back to YAML string
    return yaml.dump(extracted, allow_unicode=True, sort_keys=False)


# Extract module name from file
def get_module_names(input_str):
    file_list = input_str.split()
    result = {"zh": [], "en": []}
    
    for file_path in file_list:
        if file_path.startswith('docs/zh/'):
            for module, module_name in MODULES.items():
                if module in file_path:
                    result['zh'].append(module_name)
        elif file_path.startswith('docs/en/'):
            for module, module_name in MODULES.items():
                if module in file_path:
                    result['en'].append(module_name)
    
    return result


class MergedDict(TypedDict):
    pass


def merge_lists(list1: List[Union[MergedDict, Any]], list2: List[Union[MergedDict, Any]]) -> List[
    Union[MergedDict, Any]]:
    # Merge two lists, recursively merge if the list items are dictionaries
    result = list1.copy()
    for item in list2:
        if isinstance(item, dict):
            for existing_item in result:
                if isinstance(existing_item, dict) and set(existing_item.keys()) == set(item.keys()):
                    existing_item = deep_merge(existing_item, item)
                    break
            else:
                result.append(item)
        elif item not in result:
            result.append(item)
    return result


def deep_merge(dict1: MergedDict, dict2: MergedDict) -> Union[MergedDict, None]:
    # Recursively merge two dictionaries
    result = dict1.copy()
    for key, value in dict2.items():
        if key in result:
            if isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = deep_merge(result[key], value)
            elif isinstance(result[key], list) and isinstance(value, list):
                result[key] = merge_lists(result[key], value)
            else:
                result[key] = value
        else:
            result[key] = value
    return result


def merge_yamls(yaml_contents: List[str]) -> str:
    # Merge multiple YAML contents into one
    merged_data = {}
    for content in yaml_contents:
        yaml_data = yaml.safe_load(content)
        merged_data = deep_merge(merged_data, yaml_data)
    return yaml.dump(merged_data, allow_unicode=True, sort_keys=False)


if __name__ == '__main__':
    
    # Read the list of changed files from environment variables
    changed_files = os.environ['CHANGED_FILES']
    print(changed_files)
    
    # Extract changed modules
    module_names = get_module_names(changed_files)
    
    for lang in module_names:
        yaml_contents = []
        yaml_file_path = f"docs/{lang}/navigation.yml"
        for module_name in module_names[lang]:
            module_yaml = extract_module_from_yaml(yaml_file_path, module_name)
            yaml_contents.append(module_yaml)
        
        with open(yaml_file_path, 'w', encoding='utf-8') as file:
            file.write(merge_yamls(yaml_contents))
