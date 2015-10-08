#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import requests
import random

class Crawler:
    def __init__(self, *, log=None):
        self.logger = None
        if log is not None:
            self.logger = log.add_sub_logger(__name__)

        self.__status = None
        self.timeout = 5
        self.user_agent = ['Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',\
                           'Mozilla/5.0 (X11; Ubuntu; Linux i686;) Firefox/27.0',\
                           'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) Chrome/2.0.172.28',\
                           'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Foxy/1; InfoPath.1)',\
                           'Mobile Safari 1.1.3 (iPhone; U; CPU like Mac OS X; en)']

    def __decode(self, data, code):
        return data.content.decode(code, 'ignore')

    def __logger(self, info):
        self.logger.error(info)

    def status(self):
        return self.__status

    def get(self, url, *, params = {}, decode='utf8'):
        headers = { 'User-Agent' : random.choice(self.user_agent) }

        i = 0
        while(i<5):
            try:
                data = requests.get(url, headers=headers, params=params, timeout=self.timeout)
                self.__status = data.status_code
                return self.__decode(data, decode)
            except requests.ConnectionError as e:
                if self.logger!=None:
                    self.__logger(e)
                    self.__logger(data.url)
                i+=1
            except requests.exceptions.Timeout as e:
                if self.logger!=None:
                    self.__logger(e)
                    self.__logger(data.url)
                i+=1
        return ''    

    def post(self, url, *,  params = {}, body = {}, decode='utf8', header = {}):
        headers = { 'User-Agent' : random.choice(self.user_agent)}

        # update headers content
        if(len(header)!=0):
            headers.update(header)
        
        i=0
        while(i<5):
            try:
                data = requests.post(url, headers=headers, params=params, data=body, timeout=self.timeout)
                self.__status = data.status_code
                return self.__decode(data, decode)
            except requests.ConnectionError as e:
                if self.logger!=None:
                    self.__logger(e)
                    self.__logger('url = {}, body = {}', data.url + data.request.body)
                i+=1
            except requests.exceptions.Timeout as e:
                if self.logger!=None:
                    self.__logger(e)
                    self.__logger('url = {}, body = {}', data.url + data.request.body)
                i+=1
        return ''


"""
if __name__=="__main__":
    test = Crawler()
    print(test.post("http://www.twse.com.tw/ch/trading/exchange/MI_INDEX/MI_INDEX.php?download=csv&qdate=104/05/27&selectType=01", decode="big5"))
"""
