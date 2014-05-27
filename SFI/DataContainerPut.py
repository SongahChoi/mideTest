#!/usr/bin/env python

import Mobigen.DataProcessing.DataContainer3 as DataContainer

dc = DataContainer.DataContainer(".", Mode="a", KeepHour=4, Version=3)
for i in range(0, 1000) :
	dc.put("20120426150000", "test %10d" % i)
dc.close()
