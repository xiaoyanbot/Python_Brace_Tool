Python Brace Tool
=================

Comment style braces parser for python

Simple but useful "braces" for python:

Example:
--------
see before.py

Usage:
-------

<code>python brace.py < before.py > after.py</code>

Before:
-------
<code>

class myclass:#[
def __init__(self):#[
for i in range(10):#[
print i
#]
#]
#]

c = myclass()

</code>

After:
-------
<code>

class myclass:#[
    def __init__(self):#[
        for i in range(10):#[
            print i
        #]
    #]
#]


c = myclass()

</code>





