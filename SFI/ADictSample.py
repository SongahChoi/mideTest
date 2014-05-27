#!/usr/bin/env python

import AdvancedHashStore as AHS

table = 'test_table' #생성할 테이블 이름
server = {}
server["90.90.70.111"] = 70000 # IP, Port

dict = AHS.Client(server)

# Create Table
result = dict.create(table, "store") # store:기존 Dict 형태, 추후 다른 형태 제공 예정
if result[:3] == "nok" : print "Fail.."
else : print "Success"


# Set Data
time = "" # reserved
key = "01012341234"
value = "value"

record = {}
record[key] = [time, value]

result = dict.set(table, key, time, value)
if result[:3] == "nok" : print "Fail..."
else : print "Success..."


# Multi Set Data
result = dict.mset(table, record) 
if result[:3] == "nok" : print "Fail..."
else : print "Success..."


# Get Data
time = "" # reserved
opt = "0" # reserved
key = "01012341234"

record = {}
record[key] = [time, opt]

result = dict.get(table, key, time, opt)
if result[:3] == "nok" : print "Fail..."
else : print result


# Multi Get Data
result = dict.mget(table, record) 
if result[:3] == "nok" : print "Fail..."
else : print result


# Truncate Table
result = dict.truncate(table)
if result[:3] == "nok" : print "Fail..."
else : print "Success"


# Drop Table
result = dict.drop(table)
if result[:3] == "nok" : print "Fail..."
else : print "Success"

dict.close()


test01
test02
