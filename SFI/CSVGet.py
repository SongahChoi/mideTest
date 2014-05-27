#!/usr/bin/env python

import Mobigen.DataProcessing.CSV2 as CSV

csv = CSV.Reader(".", CSV.PARTITION, Mode="r")
#csv.setLast()
csv.SetPosition("20120507150000", 10)
csv.EnableSplit(False)

while (True) :
	data = csv.next()
	print data

csv.Close()

#test01
#test02
#test03
