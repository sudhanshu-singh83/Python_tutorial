marks = {
    "Sudhanshu" : 99,
    "Aman" : 46,
    "Rohan" : 64,
    45 : "Shyam",
}

print(marks.items()) # It returns a view containing all key-value pairs in the dictionary.

print(marks.keys()) # print all things written on LHS side

print(marks.values()) # print all th ings written on RHS side 

marks.update({"Sudhanshu" : 100 , "Ram" : 55}) # this updates the existing values and adds new key and value if it doesnt exist
print(marks) # this update marks of sudhanshu and adds a new key named Ram and value as 55 bcz it didnt existed already

print(marks.get("Anuj")) # return none bcz no key named Anuj present
print(marks["Anuj"]) # return error bcz no key named Anuj present