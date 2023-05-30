# 1. Input a welcome message and display it.

# mssg = input("Enter the welcome message : ")
# print(f"Hello, {mssg}")

# 2. Input two numbers and display the larger / smaller number.

# num1 = int(input("Enter Number one: "))
# num2 = int(input("Enter Number two : "))

# if num1 > num2:
#     print(f"{num1} is greater and {num2} is smaller")
# else:
#     print(f"{num2} is greater and {num1} is smaller")

# 3. Input three numbers and display the largest / smallest number.

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# num3 = int(input("Enter number 3: "))
# print("Largest number is: ", max(num1, num2, num3))
# print("Smallest number is: ", min(num1, num2, num3))


# 4. Generate the following patterns using nested loops:
# PATTERN 1
# for i in range(5):
#     print((i+1) * "*")

# PATTERN 2
# n = 5

# for i in range(n):
#     for j in range(i):
#         print(end='')
#     for j in range(n-i):
#         print(j+1, end='')
#     print()

# PATTERN 3
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(chr(j + 65), end="")
#     print()


# 5. Write a program to input the value of x and n and print the sum of the following series:
# SERIES 1
# x = int(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))

# sum = 0

# for i in range(0, n+1):
#     sumofseries = x ** i
#     sum += sumofseries

# print(sum)

# SERIES 2

# x = int(input("Enter value of x:"))
# n = int(input("Enter value of n:"))
# s = 0
# j = 0
# for i in range(n+1):
#     j = (-1)**i
#     k = j*(x**i)
#     s = s+k
# print(
#     f" Sum of the series: 1-x+x ^ 2-x ^ 3+x ^ 4 + ............x ^ n is = {s}")

# SERIES 3

# x = int(input("Enter the value of x: "))
# n = int(input("Enter the value of n: "))

# sum = 0

# for i in range(1, n+1):
#     sumofseries = x ** i / i
#     sum += sumofseries

# print(sum)


# SERIES 4
# n = int(input("Enter the value of n: "))

# x = int(input("Enter the value of x:  "))

# s, f, c = x, 2, 1

# for i in range(2, n+1):

#     s += c*(x ** i)/f
#     f = f * (i+1)
#     c *= -1

# print("Sum: ", s)


# 6. Determine whether a number is a perfect number, an Armstrong number or a palindrome.
# n = int(input("Enter any number to check whether it is perfect ,armstrong or palindrome  : "))
# sum = 0
# # Check for perfect number
# for i in range(1, n):
#     if n % i == 0:
#         sum = sum + i

# if sum == n:
#     print(n, "is perfect number")
# else:
#     print(n, "is not perfect number")
# # check for armstrong number
# temp = n
# total = 0
# while temp > 0:
#     digit = temp % 10
#     total = total + (digit**3)
#     temp = temp//10
# if n == total:
#     print(n, "is an armstrong number")
# else:
#     print(n, "is not armstrong number")
# # check for palindrome number
# temp = n
# rev = 0
# while n > 0:
#     d = n % 10
#     rev = rev * 10 + d
#     n = n//10
# if temp == rev:
#     print(temp, "is palindrome number")
# else:
#     print(temp, "is not palindrome number")


# 7. Input a number and check if the number is a prime or composite number
# Input a number and check if the number is prime or composite number
# n = int(input("Enter any number:"))
# if(n == 0 or n == 1):
#     print(f"{n},Number is neither prime nor composite")
# elif n > 1:
#     for i in range(2, n):
#         if(n % i == 0):
#             print(n, "is a composite number")
#             break
#     else:
#         print(n, "is a prime ")
# else:
#     print("Please enter positive number  ")


# 8. Display the terms of a Fibonacci series
# n = int(input("Enter the number of terms for the sequence "))

# n1, n2 = 0, 1
# count = 0

# if n <= 0:
#     print("Please enter a positive integer")
# elif n == 1:
#     print("Fibonacci sequence upto", n, ":")
#     print(n1)
# else:
#     print("Fibonacci sequence:")
#     while count < n:
#         print(n1)
#         nth = n1 + n2
#         n1 = n2
#         n2 = nth
#         count += 1


# 9. Compute the greatest common divisor and least common multiple of two integers.
# num1 = int(input(" Please Enter the First Value  Num1 : "))
# num2 = int(input(" Please Enter the Second Value Num2 : "))

# p = num1
# q = num2
# lcm = 0
# while(num2 != 0):
#     temp = num2
#     num2 = num1 % num2
#     num1 = temp

# gcd = num1
# lcm = ((p*q)/gcd)
# print("\n GCD or HCF of ", p, " and ", q, " = ", gcd)
# print("\n LCM of ", p, " and ", q, " = ", lcm)

# 10. Count and display the number of vowels, consonants, uppercase, and lowercase characters in the string.
# s = input("Enter any string :")
# vowel = consonent = uppercase = lowercase = 0
# for i in s:
#     if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
#         vowel = vowel + 1
#     else:
#         consonent = consonent + 1
#     if i.isupper():
#         uppercase = uppercase + 1

#     if i.islower():
#         lowercase = lowercase + 1

# print("Total number of vowel:", vowel)
# print("Total number of consonent:", consonent)
# print("Total number of uppercase letter:", uppercase)
# print("Total number of lowercase letter:", lowercase)

# 11. Input a string and determine whether it is a palindrome or not; convert the case of characters in string
# s = input("Enter any string :")
# j = -1
# flag = 0
# for i in s:
#     if i != s[j]:
#         flag = 1
#         break
#     j = j - 1
# if flag == 1:
#     print(s, "--> This string is not palindrome")
# else:
#     print(s, "--> This string is palindrome")
# sc = s.swapcase()
# print("String after converting the case of each character :", sc)


# 12. Find the largest/smallest number in a list/tuple
# list = []

# num = int(input("Enter number of elements in list: "))

# for i in range(1, num + 1):

#     element = int(input("Enter elements: "))

#     list.append(element)

# print("Smallest element in the created List is:", min(list))
# print("Largest element in the created List is:", max(list))

# 13. Input a list of numbers and swap elements at the even location with the elements at the odd location.
# mylist = []
# n = int(input("Enter (odd) number of elements to add in the list: "))

# print("Enter elements for the list: ")
# for i in range(n):
#     value = int(input())
#     mylist.append(value)
# print("The original list : " + str(mylist))
# odd_i = []
# even_i = []
# for i in range(0, len(mylist)):
#     if i % 2:
#         even_i.append(mylist[i])
#     else:
#         odd_i.append(mylist[i])
# result = odd_i + even_i
# print("Separated odd and even index list: " + str(result))

# 14. Input a list/tuple of elements, and search for a given element in the list/tuple.

# list = []
# e = input("Would you like to input (numbers) as elements or (strings)?: ")
# n = int(input("Enter number of elements to add in the list: "))
# if e == "numbers":
#     print("Enter elements to add in the list: ")
#     for i in range(n):
#         value = int(input())
#         list.append(value)
#     print("Enter an element to search in the created list: ")
#     element = int(input())
#     for i in range(n):
#         if element == list[i]:
#             print("Element is at Index:", i)
#             print("Element is at Position:", i+1)
# else:
#     print("Enter elements to add in the list: ")
#     for i in range(n):
#         value = (input())
#         list.append(value)
#     print("Enter an element to search in the created list: ")
#     element = (input())
#     for i in range(n):
#         if element == list[i]:
#             print("Element found at Index:", i)
#             print("Element found at Position:", i+1)


# 15. Create a dictionary with the roll number, name, and marks of n students in a class and display the names of students who have marks above 75.


# no_of_students = int(input("Enter number of students: "))
# result = {}
# for i in range(no_of_students):
#    print("Enter Details of student No.", i+1)
#    roll_no_of_student = int(input("Roll No: "))
#    name_of_student = input("Student Name: ")
#    marks = int(input("Marks obtained: "))
#    result[roll_no_of_student] = [name_of_student, marks]
# print(result)
# for student in result:
#    if result[student][1] > 75:
#        print("Student's name who get more than 75 marks is/are",(result[student][0]))
