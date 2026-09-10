names = ["ram", "shyam", "rohan", 2, 4.24, True, "aman"] # this is a list not a string
print(names)
names.append("sudhanshu")
print(names)

l1 = [22, 75, 53, 4, 64, 6, 12, 8, 74]
l1.sort() 
l1.reverse()
l1.insert(3,1) # this inserts 1 at index number 3 in the list
print(l1.pop(2)) # this prints the value at given index, here its index no 2, so it print value written at index 2 i.e 53
l1.pop(2) # this pops out the value at the given index no., here on index no 2 there is 53 written so it pop out 53 and print rest of the list
print(l1)