def remove_and_strip(string, word):
    newstr= string.replace(word,"")
    return newstr.strip()
a="           this    is    me   "
b=remove_and_strip(a,"me")
print(b)
aa="   my   name   is    hamza   "
aa
print(aa)
print(aa.strip())