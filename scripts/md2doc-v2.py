#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# requirements: pandoc (https://github.com/jgm/pandoc)
# requirements: python-docx docxcompose

import os, sys
from docx import Document
from docxcompose.composer import Composer


def get_md_files(path, recursion):
    '''获取指定路径下的所有.md文件'''
    if not os.path.isdir(path):
        print('请输出正确的路径')
        exit(1)

    if recursion:
        files_name = []
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name[-3:] == '.md':
                    files_name.append(os.path.join(root, file_name))
    else:
        files_name = [i for i in os.listdir(path) if i[-3:] == ".md"]   # 不递归 仅当前目录

    return files_name


def main(path='docs/zh/docs', style='预留', result_path='docs/zh.docx'):
    """分别转换指定目录下md文件内容为docx, 并合并至同一个docx文件中"""
    path = os.path.abspath(path)
    result_path = os.path.abspath(result_path)
    if not os.path.exists(result_path):
        os.system('touch ' + result_path)

    files_name = get_md_files(path, recursion=True)
    count_max = len(files_name)
    for index, file_name in enumerate(files_name):
        os.chdir(os.path.dirname(file_name))
        print("正在转换", index + 1, "/", count_max, "当前文件:", file_name)
        cmd = 'pandoc ' + file_name + ' -o ' + file_name[:-2] + 'docx'
        try:
            os.system(cmd)
        except:
            print("转换失败, 异常的文件:", file_name)

    docx_list_name = [i[:-2]+'docx' for i in files_name]

    style_demo = Document(docx_list_name[0])
    new_docx = Composer(style_demo)
    count_max = len(docx_list_name)
    for index, word in enumerate(docx_list_name):
        print("正在合并, 已添加", index + 1, "/", count_max, "个 当前读取的文件:", word)
        if not os.path.exists(word):
            print(word, "文件不存在, 请检查md转换记录, 已跳过该文件")
            continue
        word_document = Document(word)
        if index != count_max -2:
            word_document.add_page_break()
        new_docx.append(word_document)
        new_docx.save(result_path)



if __name__ == '__main__':
    main(sys.argv[1])