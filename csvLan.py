# -*- coding: utf-8 -*-
import csv
import os
import re


# key 必须为 csv 文件第一列第一个元素
# 边读边写？减少内存使用
#
#

KeyString = "Key"
# newLine="\n"
new_line = "\n"


def save(strings, filename):

    pass


def convertToiOS(dict, filename):
    # dict 内容 {"en": {"{key}": "{content}"}, "ja": {"{key}": "{content}"}}
    # 文件内容，list 为每行文字的数组
    for key in dict.keys():
        list = []
        items = dict[key]
        for item in items:
            s = '"{key}" = "{content}";'
            # 替换变量
            text = s.format(key=item, content=items[item])
            # 将换行符转化为字符串
            text = text.replace('\n', '\\n')
            # 替换所有 [] 中括号包裹的内容为 %@
            text = re.sub(r'\[\w+\]', '%@', text)
            list.append(text)
            list.append('\n')
        outputname = '{file}-{lang}-output'.format(
            file=filename, lang=key)
        with open(outputname, 'w', newline='\n') as file:
            file.write(''.join(str(s) for s in list))
            file.close()
            pass
    pass


def readCSV(filepath):
    # filepath csv文件的路径包括文件名后缀
    with open(filepath, newline="\n") as csvfile:
        (name, ext) = os.path.splitext(filepath)
        reader = csv.DictReader(csvfile)
        # dict 的内容： {"en": {"{key}": "{content}"}, "ja": {"{key}": "{content}"}}
        dict = {}
        for key in reader.fieldnames:
            if key == KeyString:
                continue
            dict[key] = {}

        for row in reader:
            for key in dict.keys():
                dict[key][row[KeyString]] = row[key]

        convertToiOS(dict, name)

        return dict
        pass


readCSV('data-9.csv')
