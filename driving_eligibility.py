print("Hi!")

choice = input(

    "Do you wanna know if you are eligible to drive or not. Press 1 for yes and 2 for no  ")

if (choice) == ("1"):

    age = int(input("Enter your age: "))

    if (int(age) >= (18)):

        print("You are eligible to drive")

    else:

        print("You are not eligible to drive")

else:

    print("Thank you")
