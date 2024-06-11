# 1. Array Reverse Using an Extra Array (Non In-place):
def rev_arr(arr):
  rev_arr = arr[::-1]
  print(rev_arr)
arr = [1,2,3,4,5]
print(rev_arr(arr))  

# 2. Array Reverse Using a Loop (In-place):
def rev_arr2(a,start,end):
  while start<end:
    a[start],a[end] = a[end],a[end]
    start+=1
    end-=1
  
a = [1,2,3,4,5]    
print (a);
rev_arr2(a,0,len(a)-1);
print(a);

# 3. Array Reverse Inbuilt Methods (Non In-place):
original_array = [1, 2, 3, 4, 5]
reversed_array = list(reversed(original_array))
print(reversed_array)


