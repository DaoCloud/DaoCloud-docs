# /usr/bin/env python3
# -*- coding: UTF-8 -*-


"""

Author: samzong.lu
E-mail: samzong.lu@gmail.com

"""
import os
import argparse

from googletrans import Translator

from config import Config

# 初始化代理配置
os.environ['all_proxy'] = Config.ALL_PROXY

translator = Translator()


# 获取当前路径下全部需要翻译的 markdown 文档
def find_md_file():
    file_list = []
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.md'):
                full_file = os.path.join(root, file)
                file_list.append(full_file)

    return file_list


# copy 当前路径下全部需要的图片
def copy_img_file():
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                full_file = os.path.join(root, file)
                filepath, filename = os.path.split(full_file)
                save_to_path = filepath.replace('/DaoCloud-docs/docs/zh/', '/DaoCloud-docs/docs/en/')
                if not os.path.exists(save_to_path):
                    os.makedirs(save_to_path)
                new_img_file = os.path.join(save_to_path, filename)
                print(new_img_file)
                os.system('cp {} {}'.format(full_file, new_img_file))


# 全量翻译，任务执行脚本
def translate_md(markdown_file):
    filepath, filename = os.path.split(markdown_file)
    new_filepath = filepath.replace('/DaoCloud-docs/docs/zh/', '/DaoCloud-docs/docs/en/')

    if not os.path.exists(new_filepath):
        os.makedirs(new_filepath)

    new_md_file = os.path.join(new_filepath, filename)

    # 读取 markdown 文件
    with open(markdown_file, 'r') as f:
        text = f.read()

    # 获取翻译后文本
    tran_text = translator.translate(text, dest='en').text

    # 写入翻译后的 markdown 文件
    with open(new_md_file, 'w') as f:
        f.write(tran_text)


# 全量翻译
def full_translate():
    md_file_list = find_md_file()
    for md_file in md_file_list:
        print(md_file)

        if md_file in ['/Users/samzonglu/Git/daocloud/DaoCloud-docs/docs/zh/docs/dce/terms.md',
                       '/Users/samzonglu/Git/daocloud/DaoCloud-docs/docs/zh/docs/native/open.md',
                       '/Users/samzonglu/Git/daocloud/DaoCloud-docs/docs/zh/docs/native/knowledge.md']:
            continue

        try:
            translate_md(md_file)
        except Exception as e:
            print(e)
            break

    copy_img_file()


# 翻译单个文件
def translate_file(file):
    if file.endswith('.md'):
        # 准备翻译后的 markdown 文件
        filename, ext = os.path.splitext(file)
        newfile = filename + '_translated' + ext

        # 读取 markdown 文件
        with open(file, 'r') as f:
            text = f.read()

        # 获取翻译后文本
        trans_text = translator.translate(text, dest='en').text

        # 写入翻译后的 markdown 文件
        with open(newfile, 'w') as f:
            f.write(trans_text)
    else:
        print("不支持的文件类型，目前仅支持 markdown 文件")


# 翻译特定文件夹
def translate_folder(folder):
    for root, dirs, files in os.walk(folder):
        new_root = os.path.join(root, '_translated')
        if not os.path.exists(new_root):
            os.makedirs(new_root)

        for file in files:
            if file.endswith('.md'):
                md_file = os.path.join(root, file)

                print(md_file)

                with open(md_file, 'r') as f:
                    text = f.read()

                trans_text = translator.translate(text, dest='en').text

                new_md_file = os.path.join(new_root, file)

                with open(new_md_file, 'w') as f:
                    f.write(trans_text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='翻译 markdown 文件，命令行使用注意事项：\n')
    parser.add_argument('--file', metavar='file=', type=str, nargs='+',
                        help='需要翻译的文件')
    parser.add_argument('--folder', metavar='folder=', type=str, nargs='+',
                        help='需要翻译的文件文件夹')
    parser.add_argument('--full_translate', metavar='full_translate', type=bool, nargs='+',
                        help='翻译全部文档，这里需要切换到路径 Daocloud-docs/docs/zh/ 下执行')

    args = parser.parse_args()

    if args.file:
        file = args.file[0]
        print(file)
        translate_file(file)
    if args.folder:
        folder = args.folder[0]
        print(folder)
        translate_folder(folder)
    if args.full_translate:
        if args.full_translate[0]:
            full_translate()

    print(args)
