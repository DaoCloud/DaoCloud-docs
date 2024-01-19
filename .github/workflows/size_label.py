# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 14:21:11 2024

@author: Fan-Lin
"""

import os
from github import Github

# 获取环境变量
TOKEN = os.environ['GITHUB_TOKEN']
REPO_NAME = os.environ['GITHUB_REPOSITORY']
PR_NUMBER = os.environ['PULL_REQUEST_NUMBER']

# 初始化Github对象
g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)
pr = repo.get_pull(int(PR_NUMBER))

# 获取PR的更改行数
additions = pr.additions
deletions = pr.deletions
total_changes = additions + deletions

# 根据更改行数设置标签
label = ''
if total_changes <= 9:
    label = 'size/XS'
elif 10 <= total_changes <= 29:
    label = 'size/S'
elif 30 <= total_changes <= 99:
    label = 'size/M'
elif 100 <= total_changes <= 499:
    label = 'size/L'
elif 500 <= total_changes <= 999:
    label = 'size/XL'
else:
    label = 'size/XXL'

# 设置标签
pr.set_labels(label)