#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 0020 下午 16:19
# @Author  : BLKStone
# @Site    : http://blkstone.github.io
# @File    : auxiliary.py
# @Software: PyCharm

import dev_common


def extract_ftp(path):
    lreader = dev_common.ListCooker()
    scan_result = lreader.load(path)

    ftp_list = []
    count = 0
    for ele in scan_result:
        record = ele.split(' ')
        if len(record) == 1:
            continue
        else:

            if 'ftp' in record[1]:
                if 'default' not in record[1]:
                    count = count + 1
                    ftp_list.append(record[0])
                    print record
                else:
                    pass
                # print count
    print 'Total:', count

    lreader.dump(ftp_list, 'ftp_category.txt')


if __name__ == '__main__':
    path = 'report/big_result1.txt'
    extract_ftp(path)