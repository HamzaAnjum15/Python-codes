with open('logfile.txt') as f:
    c=f.read()
if 'python' in  c.lower():
      print("python is present")
else:
    print("not present")