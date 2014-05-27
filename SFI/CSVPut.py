#!/usr/bin/env python

import time
import Mobigen.DataProcessing.CSV2 as CSV

csv = CSV.Writer(".", CSV.PARTITION, Mode="a", KeepHour=24, FileTimeInterval=2, Partition="1M")
for i in range(0, 1000) :
	cur_time = time.strftime("%Y%m%d%H%M%S")
	csv.put(cur_time, "%s,%05d,test,data" % (cur_time, i))
	time.sleep(0.1)
csv.Close()
