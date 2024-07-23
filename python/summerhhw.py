import random
print("Write 'roll' to roll the dice or write anything else to stop rolling random numbers")
while True:
    roll = input("roll or stop: ")
    if roll == "roll":
        x = random.randint(1,6)
        print(x)
    else:
        break

