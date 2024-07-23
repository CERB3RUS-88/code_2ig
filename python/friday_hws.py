#Write a Python program that creates a list of integers and then iterates over the list to find and print the sum of all the numbers.
lst = []
n = int(input("Enter number of integers you want to add: "))
for i in range (n):
    num = int(input("Enter the integers: "))
    lst.append(num)
sum1 = 0
for x in lst:
    sum1 += x
print(sum1)
