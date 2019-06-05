#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Ranxf

from selenium import webdriver
brower = webdriver.Firefox()
brower.get('http://127.0.0.1:8000')
# brower.get('http://baidu.com')
assert 'Django' in brower.title

