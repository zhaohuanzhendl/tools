#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016  zhzcsp@gmail.com 

import os
import logging
from logging.handlers import RotatingFileHandler
import sys
import time
import json


LOG_DIR = "./"
#interface logger 基类
class Interface(object):

    def __init__(self, name):
        """
        初始化
        """
        self.name = name
        self.logger = None
        self.set_logger()
        self.sample = None
        self.fileInfo =None

    def get_log_level(self):
        """
        获取日志的级别
        """
        #level = logging.ERROR
        level = logging.DEBUG

        return level


    def set_logger(self):
        """
        设置日志信息
        """
        logger = None
        try:
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger = logging.getLogger('Interface')
            #获取日志级别
            level = self.get_log_level()
            logger.setLevel(level)
            log_name = self.name+'ESlogger'
            #name = '_'.join([log_name,prefix]) + '.log'
            name = log_name + '.log'
            log_file= os.path.join(LOG_DIR,name)
            log_handler= RotatingFileHandler(log_file,mode='a', maxBytes=10*1024*1024, backupCount=5)
            log_handler.setFormatter(formatter)
            logger.addHandler(log_handler)
            self.logger = logger
            self.fiLogger = logging.getLogger('checker.fileinfo')
        except Exception as err:
            print "in <set_logger> has a error: %s"%err
            self.logger = None



if __name__ == "__main__":
    pass

