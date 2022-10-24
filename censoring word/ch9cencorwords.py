words=["donkey","pagal","mota"]
with open('censor.txt','r') as f:
   c= f.read()
for word in words:
    c=c.replace(word,"&^%$#@")
    with open('censor.txt','w') as f:
       f.write(c)