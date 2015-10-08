#! /usr/bin/env python3
# @Author Hugo

import csv, logging

class IO:
    """
    def __init__(self,*,log=None):
        self.data = []
        self.logger = None
        if log is not None:
            self.logger = log.add_sub_logger(__name__)
            #self.logger.info('creating an instance of Myio')
    """
    @staticmethod
    def csv_write(data, name):
        name = name.split(".")[0]
        with open(name+".csv", 'a') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(data)

    @staticmethod
    def csv_append(data, name):
        name = name.split(".")[0]
        with open(name+".csv", 'a') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(data)

    @staticmethod
    def csv_read(data, *, delimiter=','):
        return list(csv.reader(data))

    @staticmethod
    def csvfile_read(name):
        name = name.split(".")[0]
        data = list()
        with open(name+".csv", 'r') as io_read:
            for row in csv.reader(io_read,  delimiter=','):
                if len(row) > 0:
                    data.append(row)
        return data
    """
    def read(self,name):
        with open(name, 'r') as io_read:
            text = io_read.read()
        return text    

    def write(self,name, towrite):
        with open(name, 'w') as io_write:
            io_write.writelines(towrite)

    def append(self,name, towrite):
        with open(name, 'a') as io_write:
            io_write.writelines(towrite)


    def csv_write(self, name, towrite):
        name = name.split(".")[0]
        with open(name+".csv", 'w') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(towrite)

    def csv_append(self, name, towrite):
        name = name.split(".")[0]
        with open(name+".csv", 'a') as io_write:
            w = csv.writer(io_write,  delimiter=',')
            w.writerows(towrite)

    def html_write(self, name, towrite):
        with open(name+".html", 'w') as io_write:
            io_write.writelines(towrite+"\n")


    def html_append(self, name, towrite):
        with open(name+".html", 'a') as io_write:
            io_write.writelines(towrite+"\n")

    """
