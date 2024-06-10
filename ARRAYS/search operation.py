def FindElement(arr,n,key)
for(i in range(n)):
if (arr[i] == key) :
  return i;
return -1;

arr = [1,2,3,4,5]
n = len(arr)
key = 5

index = FindElement(arr,n,key)
if index != -1 :
  print("The element is found at " ,(str(index+1));
else :
  print("The element is not fount")
  
  


