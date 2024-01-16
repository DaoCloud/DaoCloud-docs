# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 15:17:40 2024

@author: FanLin

"""

'''
前提条件：安装 request 和 pandas 库
安装方法：终端输入：pip install requests
pip install pandas
需要替换填写的内容：token 和保存路径
'''

import requests
import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# 你的GitHub令牌
token = "替换为你的token"
# 你要查询的仓库名和所有者名
repo = "DaoCloud/DaoCloud-docs"
# 指定日期范围，这里以2023年1月为例
start_date = "2023-01-01T00:00:00Z"
end_date = "2023-01-31T23:59:59Z"
# GitHub的API endpoint
url = f"https://api.github.com/repos/{repo}/pulls"

headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
}

params = {
    "state": "all",  # 获取所有的PR
    "sort": "created",
    "direction": "desc",  # 从新到旧排序
    "per_page": 100,  # 每页的结果数量
}

# 创建一个DataFrame来存储结果
df = pd.DataFrame(columns=["Date", "Author", "Title", "Labels", "Label Count", "Changed Files", "Additions", "Deletions", "PR Link"])

def get_pr_details(pr):
    pr_url = pr["url"]
    pr_response = requests.get(pr_url, headers=headers)
    pr_data = pr_response.json()
    
    changed_files = pr_data["changed_files"]
    additions = pr_data["additions"]
    deletions = pr_data["deletions"]
    
    # Extract the names of all labels
    labels = [label["name"] for label in pr["labels"]]
    
    created_at_naive = datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    
    return {
        "Date": created_at_naive,
        "Author": pr["user"]["login"],
        "Title": pr["title"],
        "Labels": labels,
        "Label Count": len(labels),
        "Changed Files": changed_files,
        "Additions": additions,
        "Deletions": deletions,
        "PR Link": pr["html_url"]
    }

page = 1
with ThreadPoolExecutor(max_workers=10) as executor: 
    while True:
        params["page"] = page
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        if not data:
            break
        futures = [executor.submit(get_pr_details, pr) for pr in data if pr["created_at"] >= start_date and pr["created_at"] <= end_date]
        for future in futures:
            df = df.append(future.result(), ignore_index=True)
        page += 1

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Monthly PR details
label_counts_monthly = df["Labels"].explode().value_counts()
monthly_user_counts = df.groupby([df.index.year, df.index.month])['Author'].value_counts()

#替换保存路径
with pd.ExcelWriter('D:\图片\联想截图\\PR_detail_2023_test.xlsx') as writer: 
    df.to_excel(writer, sheet_name='PR Details')
    label_counts_monthly.to_excel(writer, sheet_name='Label Counts')
    monthly_user_counts.to_excel(writer, sheet_name='Monthly User Counts')

print(f"Total PR count for January 2023: {len(df)}")