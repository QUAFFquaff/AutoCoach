#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 3/12/2020 16:53
# @Author  : Haoyu Lyu
# @File    : DBcontroller.py
# @Software: PyCharm
import datetime
import re
import time

import MySQLdb

import numpy as np
class DBController():
    def __init__(self):
        '''connect to db'''
        self.conn = MySQLdb.connect(host='autocoach.cexuitmi8ofq.us-west-1.rds.amazonaws.com',

                               user='admin',

                               passwd='password',

                               database='ourdata',

                               charset='utf8')

    def send_data(self,filter_merge_data=[['Testid', 'test_name', '1', '1', '1', 'o_x', 'o_y', 'o_z', 'str(datetime.time)']]):
        cursor = self.conn.cursor()
        # filter_merge_data = [['Testid', 'test_name', '1', '1', '1', 'o_x', 'o_y', 'o_z', 'str(datetime.time)']]
        filter_merge_len = len(filter_merge_data)
        for x in range(filter_merge_len):
            try:

                temp = filter_merge_data[x]
                pattern = re.compile(r'[\'](.*?)[\']', re.S)
                temp = re.findall(pattern, temp)
                sql = "INSERT INTO rawdata VALUES('" + temp[0] + "','" + temp[1] + "','" + temp[2] + "','" + temp[
                    3] + "','" + temp[4] + "','" + temp[5] + "','" + temp[6] + "','" + temp[7] + "','" + temp[
                          8] + "' );"
                print(sql)
                cursor.execute(sql
                               )
                # insert data
                self.conn.commit()
            except Exception as e:
                print('Insert Failed')
                print(e)

        # close
        self.conn.commit()
        cursor.close()
        self.conn.close()

    def read_data(self):
        try:
            f = open('test.txt')
            data = f.read()
            pattern = re.compile(r'[[](.*?)[]]', re.S)
            data = re.findall(pattern,data)

            print(data[0])
            print(data[0][0])
        except Exception as e:
            print(e)
        finally:
            f.close()
        return data


    def save_data(self):
        l1 =np.array([['realtime', 'test_name', '1', '1', '1', 'o_x', 'o_y', 'o_z',str(time.time())]])
        print(l1)
        f = open('test.txt', 'a')
        for lines in l1:
            f.writelines(str(lines))
        f.close()



temp = DBController()
temp.save_data()
data = temp.read_data()
temp.send_data(data)