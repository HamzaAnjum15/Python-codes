def index_(num,arr):
    for i in arr:
            if num in arr:
                print (f"at index: {arr.index(num)}")
                return 
            else:
               return -1
            
arr1 = [1,2,3,4,5]
a =index_(5,arr1)