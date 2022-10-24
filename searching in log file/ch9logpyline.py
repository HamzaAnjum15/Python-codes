c=True
i=1
with open('logfile.txt') as f:
       while c:
                 c=f.readline()
                 if 'python' in  c.lower():
                  print(c)
                 print(f"python is present on line {i}")
                 i+=1