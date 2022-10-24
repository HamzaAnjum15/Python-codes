with open('copytext.txt') as f:
    c=f.read()
with open('textcopied.txt','w') as f:
    f.write(c)