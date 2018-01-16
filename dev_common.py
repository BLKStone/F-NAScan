#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/30 0030 下午 21:20
# @Author  : BLKStone
# @Site    : http://blkstone.github.io
# @File    : dev_common.py
# @Software: PyCharm

import validators

import socket
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

    # 注意在读取时
    # 如果该行存在 '####' 则会被忽略
    def load(self, path='default.txt'):
        python_list = []
        print('loading... ' + path)
        with open(path, 'r') as f:
            for line in f.readlines():
                # '####' for comment
                if '####' in line:
                    continue
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


class FNAParser(object):
    def __init__(self):
        pass

    def ftp_parse(self, input, output='ftp_hydra.txt'):
        '''
        hydra -L dict/ftp_username.txt -P dict/top100.txt -e ns 192.168.0.1 ftp
        hydra -L dict/ftp_username.txt -P dict/top100.txt -e ns ftp://[10.15.44.172/24]/
        hydra -L dict/ftp_username.txt -P dict/top100.txt -e ns -M report/ftp.txt -o hydra_output.txt -Vv ftp
        '''
        lreader = ListCooker()
        fna_ftp_list = lreader.load(input)
        result = []
        for ele in fna_ftp_list:
            result.append(ele.split(' ')[0].strip())
        lreader.dump(result, output)


# 域名检查器
# 检查域名(字符串)是否合法
# 判断一个字符串是否是域名
class DomainChecker(object):
    def __init__(self):
        pass

    # 判断字符串是否为数字
    @staticmethod
    def is_number(string):
        try:
            num = int(string)
        except Exception,e:
            return False
        return True

    # 判断字符串是否为IP
    @staticmethod
    def is_ip_format(string):
        try:
            socket.inet_aton(string)
            # legal
        except Exception, e:
            # illegal
            return False
        return True

    # 是否是主机，或域名
    @staticmethod
    def is_host(string):
        if string is None:
            # 排除 None 的情况
            # print "domain?", 'false'
            return False
        else:
            if not DomainChecker.is_number(string):
                # 不是数字 不是None
                if DomainChecker.is_ip_format(string):
                    # 该字符串是 ip
                    # print 'domain?', 'ip', row[0].value
                    return False
                else:
                    # 使用 validator 进一步确认域名
                    flag = validators.domain(string)
                    if flag:  # flag 为 True
                        # print 'domain?', flag, row[0].value
                        return True
                    else:
                        return False
            else:
                # 数字(端口号)排除
                # print 'domain?', 'number'
                return False


# DNS解析器
# 将域名转换为IP
class DNSAnalyzer(object):
    def __init__(self):
        pass

    @staticmethod
    def lookup(domain):
        ip = ''
        try:
            ip = socket.gethostbyname(domain)
        except Exception,e:
            return 'DNS_Resolve_Error'
        return ip











