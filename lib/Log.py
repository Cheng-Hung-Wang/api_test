#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import logging
import os

class Log():
    def __init__(self, file, *,log=__name__, path="log/",console=True):

        os.makedirs(path, exist_ok=True)

        # create logger with 'log=name'
        #self.name = '.'.join([log, self.__class__.__name__])
        self.name = log

        # 創建 logger  
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # create file handler (log save path and name) which logs even debug messages
        fh = logging.FileHandler(path+file)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)

        # create console handler with a higher log level
        if console:
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            # add the handlers to the logger
            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

    def add_sub_logger(self, name):
        # 創建 logger  
        logger = logging.getLogger(self.name+"."+name)
        logger.setLevel(logging.DEBUG)
        return logger


