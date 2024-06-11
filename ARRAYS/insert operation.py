def insert(arr,ele):
  arr.append(ele)
  return arr;
arr = [1,2,3,4,5]
ele = 6
print("before insert")
print(arr)

a=insert(arr,ele)
print("after insert")
print(a)
