# Accessing characters by index in a string
def access_char_by_index(s,k):
  return s[k];
 
a = "hello"
index = 1
print(access_char_by_index(a,index));

# Inserting Character/String into an String
def insert(original_string,insert_string,index):
  return original_string[:index] + insert_string + original_string[index:]
print(insert("hell","o",6))

