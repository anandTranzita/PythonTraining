# python follow both indexing system forward and backward both 
str = "Tranzita System"
print(str[0]) #first index
print(str[-1]) #last index
print(str[-10])
print(str[100]) #show an Error "index out of range"
print(str[0:8]) # slicing "end point always excluded"
print(str[0:-1:2])
print(str[10:0:-1])
print(str[::2])
print(str[::-1]) 
