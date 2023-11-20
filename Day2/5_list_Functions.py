l = [3,4,5,36,"Anand",True]
print(l*2)
l1 = [3,5,6,8,9,15]

print(l+l1);
print("total no of elements : ",len(l))
print("Anand" in l)
print(12 in l)
print(max(l1))

l2 = ["Anand","Kunal", "Vivek", "Pravi", "Ashish"]
print(min(l2))
print(max(l2))

l3 = [True, False]
print(max(l3))

l2.append(45)
l2.insert(1,"Piyush")
l2.pop(1)
l2.reverse()
# l2.sort()
print(l2)

l3 = [3,6,4,1,0,5,1,7,8,15,3,25,10,2,1,45];
l3.sort() # it sort list in ascending order
l3.sort(reverse=True) # it sort list in descending order
print(l3)

l4 =[1,5,6,7]
l5 = ["Anand", "Kunal","Vivek"]
l6 = [l4,l5] # nesting of list
print(l6[1][1])
print(l6[1][2][2])