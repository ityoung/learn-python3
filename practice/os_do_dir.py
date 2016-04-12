import os, datetime
print(os.path.abspath('.'))
for f in os.listdir('.'):
    fpath = os.path.join('.', f)
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(fpath)).strftime('%Y/%m/%d %H:%M')
    ftypeflag = os.path.splitext(fpath)[1]
    if(ftypeflag == ''):
        ftype = '<DIR>'
    else:
        ftype = ''
    print("%s\t%s\t%s" % (mtime, ftype, f))

'''
copy from liaoxuefeng's github
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))
'''
