#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from lib.Crawler import Crawler
from lib.IO import IO

import sys
import json

file = "tmp.csv"

def get_param(data):
    re_data = {}

    par = data.split(",")

    if len(par[0])==0:
        return ""

    for each in par:
        each = each.split("=")
        re_data.update({each[0]:each[1]})

    return re_data

def get_body(data):
    return json.dumps(json.loads(data))

def save_data(data, code):
    res = [data[0], data[1], data[2], code]
    print(res)
    IO.csv_append([res], file.split(".")[0]+"_result")



if __name__=="__main__":
    if len(sys.argv) > 1:
        file = sys.argv[1]


    data = IO.csvfile_read(file)
    domain = data.pop(0)[1]
    data.pop(0)


    for each in data:
        crawler = Crawler()
        url = domain + each[1]
        params = {}
        body   = {}
        res = None

        if each[0].find("#")==-1 and each[2] == 'GET':
            params = get_param(each[4])
            crawler.get(url, params=params)
            res = crawler.status()
            save_data(each, res)

        if each[0].find("#")==-1 and each[2] == 'POST':
            params = get_param(each[4])
            body   = get_body(each[5])
            header = {"Content-Type":each[3]}
            crawler.post(url, params=params, body=body, header=header)
            res = crawler.status()
            save_data(each, res)




