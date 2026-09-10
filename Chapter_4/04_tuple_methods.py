a = (1, 4, 3, 34, "sudhanshu", False, 3, 3, 34, 3.4)
print(a)

b = a.count(3) # tells how many times 3 came in the tuple
print(b)

c = a.index(34) # tells the index no of 34 in the given tuple,
                # but it stops searching after finding the first no, 
                # it can't tell the index no of all the 34 present in tuple
print(c)