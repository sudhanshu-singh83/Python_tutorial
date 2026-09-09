# String slicing (positive index)
name = "Sudhanshu"
nameshort = name[0:5] #start from index 0 all the way till 5 (excluding 5)
print(nameshort)
character1 = name[1]
print(character1)



# Negative slicing (Negative index)
name = "Sudhanshu"

print(name[0:5])

print(name[-5:-1]) # this give same resul as print(name[4:8]) bcz 4:8 is the positive converted form of -5: -1
print(name[4:8])


print(name[:5]) #Advance slicing technique 
                # If nothing written before : then it means it start from 0, similarly if nothing written after : that mean it prints till last letter


# Slicing with skip value

word = "Theultimatepython"
print(word[0:9:2])