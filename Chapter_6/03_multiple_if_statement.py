a = int(input("Enter your age: "))

# If statement :1
if(a%2 == 0):
    print("a is even")
    
# If statement :2
if(a>=18):
    print("You are an adult")
    print("eligible for voting")

elif(a<0):
    print("invalid age")

elif(a==0):
    print("you are 0 years old, which is not a valid age")


else:
    print("you are not eligible for voting")

print("the end")