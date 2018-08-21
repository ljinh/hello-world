# _*_ coding = UTF-8 _*_
# python3.6 + unittest + selenium3.12.0
# author:jin date:2018/6/24

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time   : 2017/10/17 21:46
# @Author : lijunjiang
# @File   : test.py

def hello():
    return 'hello'

if __name__ == '__main__':
    print('###' * 10)
    name = input("Please input your name: ")
    print(hello() + name)
    print('###' * 10)