import random

print("Tossing a coin...")

for i in range(3):
    randomNumber = random.randint(1, 2)
    if randomNumber == 1:
        print("Round " + str(i+1) + ": Head")
    else:
        print("Round " + str(i+1) + ": Tail")