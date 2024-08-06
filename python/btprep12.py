import random
import sympy

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def fn():
    list1 = []
    enkey1 = sympy.randprime(1, 25)
    while True:
        enkey2 = sympy.randprime(1, 25)
        if enkey2 != enkey1:
            break
    enkey = enkey1 * enkey2
    list1 = [i for i in range(2, enkey)]
    
    while True:
        s = random.choice(list1)
        list1.remove(s)
        if enkey % s != 0:
            break
    
    for r in range(1, enkey):
        if pow(s, r, enkey) == 1:
            if r % 2 == 0:
                break
    
    return [s, r, enkey, enkey1, enkey2]

list1 = fn()
s, r, enkey, enkey1, enkey2 = list1

while r % 2 != 0:
    list1 = fn()
    s, r, enkey, enkey1, enkey2 = list1

print(list1)

# To avoid large number computations, use modular arithmetic and integer operations
f1 = (pow(s, r // 2, enkey) + 1) % enkey
f2 = (pow(s, r // 2, enkey) - 1) % enkey

num1 = find_gcd(f1, enkey)
num2 = find_gcd(f2, enkey)
print(num1, enkey1, num2, enkey2)
