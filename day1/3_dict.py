my_dict = {
    "name" : "Anand",
    "age" : 25,
    "city" : "Luckhnow",
    "country" : "India",
    "state" : "Uttar pradesh",

}

# we can find the value of key by "get()" method

name = my_dict.get("name");
country = my_dict.get("country");

item = my_dict.items();

my_dict.pop("state");
print(my_dict.keys());
print(my_dict.values());
print(my_dict);

