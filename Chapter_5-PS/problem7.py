# If the names of 2 friends are same; what will happen to the program in problem 6?

# If the name of 2 friends are same then it will print the key and value of second input,
# since we are using .update so it will update the language of the 1st friend and final output will 
# be the name as key and the language of the second friend with the second frined lang

d = {}

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

name = input("Enter friend name: ")
lang = input("Enter language name: ")
d.update({name: lang})

print(d)