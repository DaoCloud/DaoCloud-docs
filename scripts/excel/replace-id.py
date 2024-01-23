# Author: Fan-Lin
# 2024-01-23
#
# 此脚本可以将 Excel 某一列或多列中的 GitHub ID 批量替换为真实姓名
#
# 此脚本会用到 2 个文件：
# PR_details_2023.xlsx 这是通过 pr-report.py 导出的 PR 记录表
# id-name.txt 这是 github id 与姓名的对应关系
#
# 运行此脚本之前，需要安装 2 个库 pandas 和 openpyxl：
# pip install pandas
# pip install openpyxl

import pandas as pd

# 读取 xlsx 文件的所有 sheet
xlsx = pd.read_excel('./scripts/excel/PR_details_2023.xlsx', sheet_name=None)

# 读取 txt 文件
with open('./scripts/excel/id-name.txt', 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

# 创建一个字典来保存替换关系
replace_dict = {}
for line in lines:
    if '=' in line and '@' in line:
        author, name = line.lower().split('=')[1].split('@')
        replace_dict[author] = name.strip()  # 使用 strip() 移除末尾的换行符

# 对所有 sheet 的 Author 列进行替换处理
for sheet in xlsx.keys():
    if 'Author' in xlsx[sheet].columns:
        xlsx[sheet]['Author'] = xlsx[sheet]['Author'].str.lower().map(replace_dict).fillna(xlsx[sheet]['Author'])

# 创建一个 Excel writer 对象
writer = pd.ExcelWriter('./scripts/excel/PR_details_2023_output.xlsx')

# 将处理后的 sheets 写回 xlsx 文件
for sheet in xlsx.keys():
    xlsx[sheet].to_excel(writer, sheet_name=sheet, index=False)

writer._save()
