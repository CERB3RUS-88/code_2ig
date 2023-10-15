'''x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))
distance = (x**2+y**2)**0.5
if distance <=10:
    print("True")
else:
    print("False")
'''

'''
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print("No.s are: ",x, y)
k = x
x = y
y = k
print("Swapped elements are: ",x, y)
'''
'''
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
print("No.s are: ",x, y)
x,y = y,x
print("Swapped elements are: ",x, y)
'''
'''
n = int(input("Enter no of times to run the cmd: "))
for i in range(n):
    print("GOOD MORNING")
'''

'''
import math
hypotenuse = float(input("Enter length of ladder: "))
angle_degree = float(input("Enter the angle made by ladder: ")) 
angle_radians = math.radians(angle_degree)
sin = math.sin(angle_radians)
#sin theta = perp/hypo hoga
#perp = sin theta*hypo hoga
perpendicular = sin*hypotenuse
print("Height reached by ladder = ",perpendicular, "feet")
'''
'''
n = int(input("Enter number: "))
n2 = int(input("Enter till where to go?: "))

for i in range(n2):
    j = (n*(i+1))
    print(f"{n}x{i+1} = {j}\n",end=(""))

'''

'''
lst=[]
for i in range(5):
    numbers = float(input(f"Enter number, {i+1}: "))
    lst.append(numbers)

print(f"Max value is {max(lst)} and Min value is {min(lst)}")
'''
'''
year = int(input('Enter the year: '))

if year%4 == 0:
    print('leap year')
else:
    print('not leap year')
'''

#Important question
'''
n = int(input("Enter n: "))
for i in range (5,n+1,5):
    if i%2 != 0:
        i *= -1
    print(i,end=' ')
'''

'''
n = int(input("Enter n: "))
sum = 0
for i in range(1,n+1):
    sum += 1/i**3
    print(sum)
'''

'''
n = input("enter n: ")
sum = 0
for i in n:
    sum += int(i)
print(sum)
'''

'''
n = input("Enter number: ")
lst=[]
for i in n:
    lst.append(i)
print(lst)
lst2 = lst[::-1]
if lst2 == lst:
    print("Palindrome")
else:
    print("Not Palindrome")
    '''
'''
n = 3
for i in range(1,n+1):
    space = (n-i)*' '
    star = (2*i-1)*"*"
    print(space,star)
for x in range(n-1,0,-1):
    space2 = (n-x)*' '
    star2 = (2*x-1)*"*"
    print(space2,star2)
    '''
'''
n = 5
for i in range(1,n+1):
    space = (n-i)*' '
    print(space, end='')
    for k in range(i,1,-1):
        print(k,end='')
    for j in range(1,i+1):
        print(j,end='')
    print()
    '''
count = 0
def entry():
    username = input("Enter user id: ")
    password = input("Enter password: ")
    login(username,password)
def login(uid,pwd):
    global count
    if uid == "ADMIN" and pwd == "St0rE@1":
        print("Welcome!")
        return

    else:
        count+=1
        print("Incorrect Id or pwd ")

    if count > 2:
        print("Blocked")
        return
    else:
        entry()



entry()
            