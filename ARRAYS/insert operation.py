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

#insert at a given position
def insert2(original_list, position, element):
    if position<0 or position> len(original_list):
        raise IndexError("invalid position");
    new_list = original_list[:position] + [element] + original_list[position:]
    return new_list;

original_list = [1,2,3,4,5,6]
position = 2
element = 13
print(insert2(original_list,position,element))
