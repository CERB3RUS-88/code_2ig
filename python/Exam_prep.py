num1 = int(input("Enter number one: "))
num2 = int(input("Enter number two: "))
num3 = int(input("Enter number three: "))

if num1 > num2 and num1 > num3:
    if num2 > num3:
        print(f"{num1} is the largest number and {num3} is smallest")
    if num3 > num2:
        print(f"{num1} is the largest number and {num2} is smallest")
elif num2 > num1 and num2 > num3:
    if num1 > num3:
        print(f"{num2} is the largest number and {num3} is smallest")
    if num3 > num1:
        print(f"{num2} is the largest number and {num1} is smallest")
else:
    if num1 > num2:
        print(f"{num3} is the largest number and {num2} is smallest")
    if num2 > num1:
        print(f"{num3} is the largest number and {num1} is smallest")
