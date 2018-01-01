#This code is based on:
# curlypy.py - preprocessor for curly bracket styled python
# Copyright (c) 2008 Niall McCarroll  
# Distributed under the MIT/X11 License (http://www.mccarroll.net/snippets/license.txt)


import sys
inlines = map(lambda x:x.strip(),sys.stdin.read().split("\n"))
indent = ''
indentstr = '    '

for line in inlines:
	openblock = False
	if line.endswith("#]"):
		indent = indent[:-len(indentstr)]
                #Leave comment symbol by comment out next line
		#line = line[:-2]
	elif line.endswith("#["):
		openblock = True
                #Leave comment symbol by comment out next line
		#line = line[:-2].rstrip()
	print indent + line.rstrip(";")
	if openblock:
		indent += indentstr
