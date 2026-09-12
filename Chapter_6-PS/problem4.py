# Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")
if(len(username)<10):
    print("this username contain less than 10 character")

elif(len(username)==10):
    print("This username contain 10 character") 

else:
    print("this username contain more than or equal to 10 character")