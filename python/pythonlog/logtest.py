#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2016  zhzcsp@gmail.com

from ESinterface import *


class Logtest(Interface):
    def __init__(self):
        #Interface.__init__(self, 'summary')
        super(Logtest, self).__init__('summary')

    def onTest(self):
        
        try:
            #path = self.sample['file_path']
            #self.get_file_path()
            testlog = "hhahaha"
            self.logger.debug("Start TestLog %s" % testlog)
            ret = [1,2,3]
            
        except Exception, err:
            print "ERROR %s" % err
        return ret 

if __name__ == '__main__':
    #Logtest().run()
    lt = Logtest()
    lt.onTest()
