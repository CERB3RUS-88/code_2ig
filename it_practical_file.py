business = input("What do you sell: ")
sales1 = int(
    input(f"Enter the number of {business} sold in the month of January: "))
sales2 = int(
    input(f"Enter the number of {business} sold in the month of February: "))
sales3 = int(
    input(f"Enter the number of {business} sold in the month of March: "))
total_sales = sales1 + sales2 + sales3
print(f"Total sales = {total_sales} {business} sold")
avg_sales = int(total_sales // 3)
print(f"The average sales = {avg_sales} {business}")


# # '''even_numbers = [2, 4, 6, 8, 10]
# # print(f"Length of even numbers = {len(even_numbers)}")
# # print(f" Third even number is {even_numbers[-3]}")'''


# # # first_5_multiples_of_2 = [2, 4, 6, 8, 10]
# # # print(first_5_multiples_of_2[-4:])


# # # fruits = ["Apples", "Oranges", "Grapes", "Kiwi", "Banana"]
# # # fruits.reverse()
# # # print(fruits)


# # # numbers = [10, 11, 12, 14, 15]
# # # numbers.insert(3, 13)
# # # print(numbers)


# # # alphabets = ["a", "b", "c", "d", "e"]
# # # alphabets.append("f")
# # # alphabets.pop(2)
# # # print(alphabets)


# # # num1 = float(input("Enter first number: "))
# # # num2 = float(input("Enter second number: "))
# # # num3 = float(input("Enter third number: "))

# # # if (num1 > num2) and (num1 > num3):
# # #     largest = num1
# # # elif (num2 > num1) and (num2 > num3):
# # #     largest = num2
# # # else:
# # #     largest = num3

# # # print("The largest number is", largest)


# # # num = int(input("Enter the number:  "))
# # # if (num % 2) == 0:
# # #     print(num, "is even number")
# # # else:
# # #     print(num, "is odd number")


# # list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(list[1:-2])
# # #


# name = input("Enter your name: ")
# if name == "Shaurya":
#     print("You are welcome")
# else:
#     print("You are not allowed here")
