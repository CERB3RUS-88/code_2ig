
sum = 0
#difference = 0
product = 1
quotient = 1

print("Welcome!")
PROMPT = "ADD(+),SUBTRACT(-),MULTIPLY(*),DIVISION(/), FLOOR DIVISION(//), REMAINDER(%), SQUARE(**)"
cmd = (input(
    f"Following are the possible operations,\n{PROMPT}\nKindly enter the operation to proceed:  "))

digit_count = int(input("Enter the number of digits for the operation: "))

# num1 = int(input("Enter the number"))
for i in range(digit_count):
    if cmd.lower() == "+":
        num = float(input(f"Enter number{i+1}: "))
        sum += num
        print("Sum is:", sum)

    elif cmd.lower() == "multiply":
        num = float(input(f"Enter number{i+1}: "))
        product *= num
        print("Product is:", product)

if cmd.lower() == "-":
    num1 = float(input(f"Enter number: "))
    for i in range(digit_count-1):
        num = float(input(f"Enter number: "))
        sum += num
        difference = num1-sum
        print(difference)
        # list1.append(x)
        # # list1.sort()
        # print(list1)
        # difference = [y-num1 for y in list1]
        # print(difference)
# num1 lelena hai
