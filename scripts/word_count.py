#! /usr/bin/python3
# -*- coding: utf-8 -*-

import string
import os
import io
import re

def str_count(s):
    count_en = count_dg = count_sp = count_zh = count_pu = 0
    s_len = len(s)
    for c in s:
        # 统计英文
        if c in string.ascii_letters:
            count_en += 1
        # 统计数字
        elif c.isdigit():
            count_dg += 1
        # 统计空格
        elif c.isspace():
            count_sp += 1
        # 统计中文
        elif c.isalpha():
            count_zh += 1
        # 统计特殊字符
        else:
            count_pu += 1
    total_chars = count_zh + count_en + count_sp + count_dg + count_pu
    if total_chars == s_len:
        return ('总字数：{0},中文字数：{1},英文字数：{2},空格：{3},数字数：{4},标点符号：{5}'.format(s_len, count_zh, count_en, count_sp, count_dg, count_pu))


class MarkdownCounter:
    def __init__(self, filename):
        self.filename = filename
        self.__zh_pattern = u"[\u4e00-\u9fa5]"
        self.__zh_punctuation = u"[\u3000-\u303f\ufb00-\ufffd]"
        self.__en_pattern = u"[A-Za-z]"
        self.__digital_pattern = u"[0-9]"
        self.__whitespace = u"[ \t\n\r\f\v]"
        self.__others_pattern = "(?!" + self.__zh_pattern + "|" + self.__zh_punctuation + "|" + self.__en_pattern + "|" + self.__digital_pattern + "|" + self.__whitespace + ")"

    def __read_file(self):
        with io.open(self.filename, mode='r', encoding='utf-8') as md_file:
            self.content = md_file.read()

    def count_words(self):
        self.__read_file()
        unicode_content = self.content
        re.split
        zh_content = re.findall(self.__zh_pattern, unicode_content)
        zh_punc_content = re.findall(self.__zh_punctuation, unicode_content)
        en_content = re.findall(self.__en_pattern, unicode_content)
        dig_content = re.findall(self.__digital_pattern, unicode_content)
        whitespace_content = re.findall(self.__whitespace, unicode_content)
        others_content = re.findall(self.__others_pattern, unicode_content)
        self.zh_len, self.zh_punc_len, self.en_len, self.digital_len, self.whitespace_len, self.others_len = len(zh_content), len(zh_punc_content), len(en_content), len(dig_content), len(
            whitespace_content), len(others_content)


if __name__ == "__main__":
    print("markdown word counter!")
    print(os.getcwd())

    # sample file 'README.md'
    # with io.open("README_zh.md", mode='r', encoding='utf-8') as md_file:
    #     buffer = md_file.read()
    #     out = str_count(buffer)
    #     buffer_unicode = buffer.encode('utf-8')

    # counter = MarkdownCounter("README_zh.md")
    # counter.count_words()
    # print(counter.content.encode('utf-8'))
    # print("中文: {}, 中文标点: {}, 英文: {}, 数字: {}, 空格: {}, 其他: {}".format(counter.zh_len, counter.zh_punc_len, counter.en_len, counter.digital_len, counter.whitespace_len, counter.others_len))
    

    # all files
    all_files_count_zh = all_files_count_en = 0

    for root,dirs,files in os.walk(os.getcwd()):
        for file in files:
            if file.endswith('.md'):
                file = root + '/' + file
                with io.open(file, mode='r', encoding='utf-8') as md_file:
                    buffer = md_file.read()
                    out = str_count(buffer)
                    buffer_unicode = buffer.encode('utf-8')

                counter = MarkdownCounter(file)
                counter.count_words()
                all_files_count_zh += counter.zh_len
                all_files_count_en += counter.en_len
    
    print('全部中文字符数：',all_files_count_zh,'全部en字符数：', all_files_count_en)