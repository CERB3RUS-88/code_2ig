
sum = 0
#difference = 0
product=1
quotient = 1
exp_product = 1

print("Welcome!")
PROMPT = "ADD(+),SUBTRACT(-),MULTIPLY(*),DIVISION(/), FLOOR DIVISION(//), REMAINDER(%), SQUARE(**)"
cmd = (input(f"Following are the possible operations,\n{PROMPT}\nKindly enter the operation to proceed:  "))

digit_count = int(input("Enter the number of digits for the operation: "))

for i in range (digit_count):
    if cmd.lower() == "+":
        num = float(input(f"Enter number{i+1}: "))
        sum+=num
        print("Sum is:", sum)


    elif cmd.lower() == "*":
        num = float(input(f"Enter number{i+1}: "))
        product*=num
        print("Product is:", product)
    
        
if cmd.lower() == "**":
    base_value = float(input("Enter base value: "))
    for i in range(digit_count -1):
        num = float(input(f"Enter exponential value {i+1}: "))
        product *= num
        exp_product = base_value**product
        print(exp_product)

elif cmd.lower() == "/":
    dividend = float(input("Enter the dividend: "))
    for i in range (1,digit_count):
        divisor = float(input("Enter the divisor(s): "))
        quotient = dividend/divisor
        print(quotient)

        



elif cmd.lower() == "-":
    num1 = float(input(f"Enter number: "))
    for i in range(digit_count-1):
        num = float(input(f"Enter number: "))
        sum += num
        difference = num1-sum
    print("Difference is ", difference)
    
    




    


























#wrong attempt
#    elif cmd.lower() == "-":
#        list1 = []
#        for z in range (digit_count):
#            x = float(input(f"Enter number{i+1}: "))
#
#            list1.append(x)
#            difference = x - list1


        #print(list1)
        #for i in list1:

            
            #val = list1(0)
            #difference = list1(0)-list1
            #print(difference)


        #num = -(num)
        #difference=(num-difference)
        #print("difference is:", difference)

