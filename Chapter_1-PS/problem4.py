import os
# select the directory whose content you want to list
directory_path = "/"

contents = os.listdir(directory_path)
# use the os module to list the directory content
for item in contents:
# prints the content of the directory
    print(item)