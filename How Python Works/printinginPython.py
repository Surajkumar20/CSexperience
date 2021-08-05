import time as t

# Basic print function
print("I am using the print function by itself\n")

# Printing using the format function
print("This is how you use the {} function, name: {}".format("format()", "Suraj"))

# How to use \r
i = 0
while (i < 15):
    i = i + 1
    if i > 9:
        print('This is the value of i: {}'.format(i))
        break
    print("This is the value of i: {}".format(i), end = "\r")
    t.sleep(0.5)

# How to use the rstrip() function
print("\n")
string = "This function will remove all white spaces from the right edge of this string         \n"
print(string.rstrip())

# How to use the + feature to concatenate strings
string_1 = "\nThis is how to "
string_2 = "concatenate two strings together"
print(string_1 + string_2)

# The str() function is necessary to concatenate numbers
string_1 = "My age is "
print(string_1 + str(21))