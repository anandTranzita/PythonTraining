my_List = [1,2,3,"Rohan", "karan"];

#  "append" operation(it add element at the last index);
my_List.append(4);
my_List.append(5);

for i in range(6,10):
    my_List.append(i);
print(my_List);

# "extend" is use to add more then one element in the list
my_List.extend([15,10,"Shyam"]);
print(my_List);


# "insert" is use to add element at any point
my_List.insert(0,"Anand");
print(my_List);

# "remove" is use to delete element 
my_List.remove("Shyam");
my_List.remove(2);
print(my_List);

# "pop" is used to delete elememt at given index
my_List.pop(0);
my_List.pop(1);

print(my_List);