# -*- coding: utf-8 -*-
#
# Created on Tue Jan 16 15:17:40 2024
# @author: FanLin
#
# 此脚本会导出 repo 下的所有 PR 记录，方便汇总统计
#
# 需要安装 request 和 pandas 库：
# pip install requests
# pip install pandas
#
# 默认导出到 repo 根目录

import requests
import pandas as pd
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# 你的 GitHub 令牌
token = "替换为你的 token"
# 要查询的仓库名
repo = "DaoCloud/DaoCloud-docs"
# 指定要导出的日期范围
start_date = "2023-01-01T00:00:00Z"
end_date = "2023-01-31T23:59:59Z"
# GitHub 的 API endpoint
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

def get_pr_details(pr):
    pr_url = pr["url"]
    try:
        pr_response = requests.get(pr_url, headers=headers)
        pr_data = pr_response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching PR details for {pr_url}: {e}")
        return None
    
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

def fetch_all_prs(url, headers, params, start_date, end_date):
    df = pd.DataFrame(columns=["Date", "Author", "Title", "Labels", "Label Count", "Changed Files", "Additions", "Deletions", "PR Link"])
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
                result = future.result()
                if result is not None:
                    df = df.append(result, ignore_index=True)
            page += 1
    return df

# 获取所有 PR
df = fetch_all_prs(url, headers, params, start_date, end_date)

df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# Monthly PR details
label_counts_monthly = df["Labels"].explode().value_counts()
monthly_user_counts = df.groupby([df.index.year, df.index.month])['Author'].value_counts()

# 替换保存路径
with pd.ExcelWriter('PR_detail_2023.xlsx') as writer: 
    df.to_excel(writer, sheet_name='PR Details')
    label_counts_monthly.to_excel(writer, sheet_name='Label Counts')
    monthly_user_counts.to_excel(writer, sheet_name='Monthly User Counts')

print(f"Total PR count for January 2023: {len(df)}")
