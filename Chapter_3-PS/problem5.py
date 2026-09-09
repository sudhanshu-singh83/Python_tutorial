# Write a program to format the following letter using escape sequence characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear \"Harry\",\n\tthis python course is nice.\nThanks!"
# here \n is used for new line , \t is used for tab
# and \"  \" is used for adding duoble quote, \ is added before " so that python doesn't consider it as a string
print(letter)