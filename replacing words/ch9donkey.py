with open('donkey.txt','r') as f:
    c= f.read()
    c=c.replace("donkey","monkey")
    with open('donkey.txt','w') as f:
       f.write(c)