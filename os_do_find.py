'''
Created on 2016-3-15

@author: young
'''
import os

list = []
#pwd = os.path.abspath('.')
pwd = '.'

def find(key, path = pwd):
    if os.path.isdir(path):
        for f in os.listdir(path):    #list all filename path contains
            fpath = os.path.join(path, f)
            find(key, fpath)
    elif key in os.path.basename(path):    #equal to os.path.split(path)
        print(path)

if __name__ == '__main__':
    print('Please input what you want to search: ')
    key = input('keyword: ')
#    path = input('path: ')
    find(key)
    
