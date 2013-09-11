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

path1 = 'F:/My Dropbox/RIA/2013_08_06_MoscowElections/data/RayonsKeys2.csv'
dataSet = p_fileWrangler.readRows(path1)
dataSet.pop(0) # remove header
path = 'F:/My Dropbox/RIA/2013_08_06_MoscowElections/data/RayonsKeys2.xml'

data = etree.Element('data')
rs = etree.SubElement(data, 'rs')


#regions
for row in dataSet:
  rowArray = row.decode('utf-8').replace('\n', '').split(';')
  r = etree.SubElement(rs, 'r')

  rid = etree.SubElement(r, 'rid')
  rid.text = rowArray[1]

  t = etree.SubElement(r, 't')
  t.text = rowArray[0]


et = etree.ElementTree(data)
et.write(path, pretty_print=True, encoding = 'utf-8')
print 'done!'
