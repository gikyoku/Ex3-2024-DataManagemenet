import random

print("Tossing a coin...")
headcount = 0
for i in range(3):
    randomNumber = random.randint(1, 2)
    if randomNumber == 1:
        print("Round " + str(i+1) + ": Head")
        headcount = headcount + 1
    else:
        print("Round " + str(i+1) + ": Tail")
print("Heads: " + str(headcount) + ", Tails: " + str(3 - headcount))