import os
oldname="sample.txt"
newname="newsample.txt"
with open('sample.txt')as f:
    c=f.read()
with open('newsample.txt','w')as f:
    d=f.write(c)
os.remove(oldname)