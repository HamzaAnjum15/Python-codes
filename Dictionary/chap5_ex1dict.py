mydict = {
   "chawal" : "rice",
   "aam" : "mango",
   "kela" : "banana" 
}
print("your options are",mydict.keys())
a = input("enter a word\n")
print("meaning: ",mydict.get(a))
