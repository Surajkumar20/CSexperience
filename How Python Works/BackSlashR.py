import time as t

i = 0
while (i < 100):
    i = i + 1
    print("This is the value of i: {}\r".format(i), end = "\r")
    t.sleep(0.5)

