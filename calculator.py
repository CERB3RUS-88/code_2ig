choice = input(
    "Do you wanna calculate something? press 1 for yes and 2 for no ")

if choice == ("1"):
    print("If you wanna calculate then enter the number of the operation you wish to do.")
    print("add = 3")
    print("subtraction = 4")
    print("multiplication = 5")
    print("division = 6")
    print("to find remainder = 7")

    choice_2 = (
        input("enter the number:  "))

    if choice_2 == ("3"):
        num1 = float(input("Enter number 1 "))
        num2 = float(input("Enter number 2 "))
        sum = (num1 + num2)
        print(sum)

    if choice_2 == ("4"):
        num3 = float(input("Enter number 1 "))
        num4 = float(input("Enter number 2 "))
        difference = (num3 - num4)
        print(difference)

    if choice_2 == ("5"):
        num5 = float(input("Enter number 1 "))
        num6 = float(input("Enter number 2 "))
        product = (num5 * num6)
        print(product)

    if choice_2 == ("6"):
        num7 = float(input("Enter number 1 "))
        num8 = float(input("Enter number 2 "))
        quotient = (num7 // num8)
        print(quotient)

    if choice_2 == ("7"):
        num9 = float(input("Enter number 1 "))
        num10 = float(input("Enter number 2 "))
        remainder = (num9 % num10)
        print(remainder)


else:
    print("Thank you have a nice day!")
