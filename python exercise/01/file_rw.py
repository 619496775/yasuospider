# -*- coding:utf-8 -*-
with open('text.txt') as f:
    print(dir(f))
    for line in f.readlines():
        print(line)

with open('text.txt','rb') as f:
    print(f.read())

s = 'abcdefg'
b = bytes(s,'utf8')
print(b)
