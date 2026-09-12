# Write a program to find out whether a given post is talking about “Harry” or not
post = input("Enter your post: ")

if("Sudhanshu".lower() in post.lower()):
    print("This post is talking about Sudhanshu")

else:
    print("This post is not talking about Sudhanshu")