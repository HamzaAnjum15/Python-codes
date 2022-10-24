f1="copytext.txt"
f2="textcopied.txt"
with open(f1) as f:
    file1=f.read()
with open(f2) as f:
    file2=f.read()
if file1==file2:
    print("the files are identical")
else:
    print("the files are not identical")
     