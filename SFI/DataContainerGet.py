#!/usr/bin/env python

import Mobigen.DataProcessing.DataContainer3 as DataContainer

dc = DataContainer.DataContainer(".", Mode="r")
ftime, mtime, opt, idx, data = dc.getLast()
#ftime, mtime, opt, idx, data = dc.get("20120407120000", 100)

while (True) :
	ftime, mtime, opt, idx, data = dc.next()
	print data

dc.close()

#test-01
