a = int(input("Enter your age: "))

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