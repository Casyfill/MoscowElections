#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import p_fileWrangler

try:
  from lxml import etree
  print("running with lxml.etree")
except ImportError:
  try:
    # Python 2.5
    import xml.etree.cElementTree as etree
    print("running with cElementTree on Python 2.5+")
  except ImportError:
    try:
      # Python 2.5
      import xml.etree.ElementTree as etree
      print("running with ElementTree on Python 2.5+")
    except ImportError:
      try:
        # normal cElementTree install
        import cElementTree as etree
        print("running with cElementTree")
      except ImportError:
        try:
          # normal ElementTree install
          import elementtree.ElementTree as etree
          print("running with ElementTree")
        except ImportError:
          print("Failed to import ElementTree from any known place")

path1 = 'F:/My Dropbox/RIA/2013_08_06_MoscowElections/data/Bld/Bld_regionsForXML8concat.csv'
dataSet = p_fileWrangler.readRows(path1)
dataSet.pop(0)
path = 'F:/My Dropbox/RIA/2013_08_06_MoscowElections/data/Uiks/UiksZones8.xml'

def xmlProduce(cell, name):
	print '<%s>%s</%s>' %(name,str(cell),name)

data = etree.Element('data')
us = etree.SubElement(data, 'us')
# count = 0


uikTemp = []

for row in dataSet:
	uikID = row.split(';')[3].strip().decode('utf-8', 'ignore')

	if uikID not in uikTemp:
		uikTemp.append(uikID)
		# print str_Rayon, ':', ID
		# print uikID
		u = etree.SubElement(us, 'u')
		id = etree.SubElement(u, 'id')
		ss = etree.SubElement(u, 'ss')
		id.text = uikID
print 'uiks done'

ds1 = dataSet
for u in us:
	# strcount+=1
	# print len(street)
	uID = u[0].text
	
	# print "!!!!!!!"

	strTemp = []
	strCOunt = 0
	for row in ds1:


		sUikID =row.split(';')[3].strip().decode('utf-8', 'ignore')
		sName =row.split(';')[1].strip().decode('utf-8', 'ignore') 
		# print sUikID, ":", uID

		if sUikID == uID and sName not in strTemp:
			# print "!"
			# strCOunt+=1
			# if strCOunt%10 == 0:
			# 	print "-"
			# elif strCOunt%5 ==0:
			# 	print "|"

			strTemp.append(sName)

			s =  etree.SubElement(u[1], 's')
			st = etree.SubElement(s, 'st')
			st.text = 	row.split(';')[1].strip().decode('utf-8', 'ignore').replace('"','')
			bs = etree.SubElement(s, 'bs')
			# ds1.remove(row)	
print 'streets done'

ds2 = dataSet
for u in us:
	# strcount+=1
	# print len(street)
	uID = u[0].text
	
		
	for s in u[1]:
		sName = s[0].text

		bldCount = 0
		for row in ds2:
			bldCount+=1
			# print "bld: ", bldCount
			 
			sUikID =row.split(';')[3].strip().decode('utf-8', 'ignore')
			rowSName =row.split(';')[1].strip().decode('utf-8', 'ignore') 	
				
			if sUikID == uID and rowSName==sName:
				b =  etree.SubElement(s[1], 'b')
				bt = etree.SubElement(b, 'bt')
				bt.text = 	row.split(';')[2].strip().decode('utf-8', 'ignore').replace('"','')
				# ds2.remove(row)	
print 'bld done'


et = etree.ElementTree(data)
et.write(path, pretty_print=True, encoding = 'utf-8')
print '     ... done!'

# print (etree.tostring(data, pretty_print=True, encoding = 'utf-8')) #.encode('utf-8')
