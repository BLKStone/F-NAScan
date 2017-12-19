#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/30 0030 下午 21:20
# @Author  : BLKStone
# @Site    : http://blkstone.github.io
# @File    : dev_common.py
# @Software: PyCharm

import datetime
import pickle


class TimeKeeper(object):
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        self.elapsed_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def stop(self):
        self.stop_time = datetime.datetime.now()

    def elapsed(self):
        self.elapsed_time = self.stop_time - self.start_time
        message = '[*] elapsed ' + str(self.elapsed_time) + '...'
        print(message)
        return self.elapsed_time


# 将 python 对象存储为文件
class ObjectCooker(object):
    def __init__(self):
        pass

    def dump(self, python_object=None, path='default.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(python_object, f)
            print('dumping... '+path)

    def load(self, path='default.pkl'):
        with open(path, 'rb') as f:
            python_object = pickle.load(f)
            print('loading... '+path)
        return python_object


# 将 List 存储为文件
class ListCooker(object):
    def __init__(self):
        pass

    def load(self, path='default.txt'):
        python_list = []
        print('loading... ' + path)
        with open(path, 'r') as f:
            for line in f.readlines():
                if line[-1] == '\n':
                    python_list.append(line[:-1])
                else:
                    python_list.append(line)
        return python_list

    def dump(self, python_list=None, path='default.txt'):
        with open(path, 'w') as f:
            print('dumping... '+path)
            for ele in python_list:
                if ele[:-1] == '\n':
                    f.write(ele.strip())
                else:
                    f.write(ele.strip()+'\n')
        f.close()


class URLAnalyzer(object):
    def __init__(self):
        pass

    # 输入 一个url的list
    # 输出 域名list
    def distinct_domains(self, url_list):
        distinct = set()
        for url in url_list:
            try:
                distinct.add(url.split('/')[2])
            except Exception, e:
                print(e)
                continue

        result = list(distinct)
        return result

    # 用于清洗来自fofa爬虫的URL
    # 输入 url 的 list
    # 输出 url 的 list (前方带完整协议标记)
    def wash_url_list(self, urls):
        wash_urls = []
        for url in urls:
            if url[:5] == 'https':
                wash_urls.append(url)
            else:
                wash_urls.append('http://' + url)
        return wash_urls









