apple = 1
banana = 1
pineapple = 1
i = 0
bar_const = 1000000
def condition():
    return(apple / (banana + pineapple) + banana / (apple + pineapple) + pineapple / (apple + banana) == 4)

while not condition():
    for apple in range(2+bar_const*i, 1000 + bar_const*(i+1)):
        if condition():
            break
        for banana in range(2+bar_const*i, 1000 + bar_const*(i+1)):
            if condition():
                break
            for pineapple in range(2+bar_const*i, 1000 + bar_const*(i+1)):
                if condition():
                    break
    i += 1

print("apple = {}, banana = {}, pineapple = {}".format(apple, banana, pineapple))