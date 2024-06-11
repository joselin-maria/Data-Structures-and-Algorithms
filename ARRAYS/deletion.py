def delete(arr, ele):
  if ele in arr:
    arr.remove(ele)
  return arr
arr = [1,2,3,4,5]
ele = 3
print("before deletion")
print(arr)

print("after deletion")
print(delete(arr,ele))
