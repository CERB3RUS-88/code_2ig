import random
username = input("Enter username: ")
str = ""
n = int(input("Enter number of digits to generate: "))
for i in range(n-2):
    x = random.randint(64, 90)
    str += chr(x)

y = random.randint(49, 57)
z = random.randint(35, 38)

# print(chr(y)+str.capitalize(),end='')
pwd = (str.capitalize()+chr(y)+chr(z))
print(pwd)
print()
dictionary = {username, pwd}
print(dictionary)
