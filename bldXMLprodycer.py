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
base = 'F:/My Dropbox/RIA/2013_08_06_MoscowElections/data/Bld/regions/regionV4'
dataSet.pop(0)

def xmlProduce(cell, name):
	print '<%s>%s</%s>' %(name,str(cell),name)

data = etree.Element('data')
rs = etree.SubElement(data, 'rs')
count = 0
rayonsTemp = []

for row in dataSet:
	# print count
	row.decode('utf-8', 'ignore')
	tempID = int(row.split(';')[0].strip())
	# print (tempID)
	if tempID not in rayonsTemp:
		count+=1
		rayonsTemp.append(tempID)

		r = etree.SubElement(rs, 'r')
		ID = etree.SubElement(r, 'ID').text = str(tempID)
		ss = etree.SubElement(r, 'ss')
print 'rayons done'


cnt = 0
for r in rs:
	rID = r[0].text
	streetsTemp = []

	for row in dataSet:
		str_Rayon = row.split(';')[0].strip()
		strName = row.split(';')[1].strip().decode('utf-8', 'ignore').replace('"','')
		if len(strName) == 0:
			strName = '-' 

		if str_Rayon == rID and strName not in streetsTemp:
			streetsTemp.append(strName)
			# print str_Rayon, ':', ID
			# print strName
			s = etree.SubElement(r[1], 's')
			t = etree.SubElement(s, 't')
			bs = etree.SubElement(s, 'bs')
			t.text = strName
print 'streets done'


ds = dataSet
for r in rs:
	rID = r[0].text
	
	# print len(rayon)
	for s in r[1]:
		# strcount+=1
		# print len(street)
		strID = s[0].text
		
		scount = 0


		for row in ds:
			scount+=1
			# print scount
			bRID =row.split(';')[0].strip().decode('utf-8', 'ignore') 
			bStrID =row.split(';')[1].strip().decode('utf-8', 'ignore') 

			if bRID == rID and bStrID == strID:

				b =  etree.SubElement(s[1], 'b')
				bt = etree.SubElement(b, 'bt')
				bt.text = 	row.split(';')[2].strip().decode('utf-8', 'ignore').replace('"','')

				u = etree.SubElement(b, 'u')
				u.text = 	row.split(';')[3].strip().decode('utf-8', 'ignore')
				# ds.remove(row)
print 'bldngs done'

for r in rs:
	ID = '_' + r[0].text
	path = base + ID +'.xml'
	et = etree.ElementTree(r)
	et.write(path, pretty_print=True, encoding = 'utf-8')
	print ID + '     ... done!'

# print (etree.tostring(data, pretty_print=True, encoding = 'utf-8')) #.encode('utf-8')
