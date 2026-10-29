import random
x = 0
y = 0
for i in range(100):
    which = random.choice(["x", "y"])
    if which == "x":
        x += random.choice([-1, 1])
    else:
        y += random.choice([-1, 1])
print("(",x,", ",y,")")