import random
def randpass():
    global pwd
    username = input("Enter username: ")
    str = ""
    n = int(input("Enter number of digits to generate: "))
    for i in range(n-2):
        x = random.randint(64, 90)
        str += chr(x)

    y = random.randint(49, 57)
    z = random.randint(35, 38)

    
    pwd = (str.capitalize()+chr(y)+chr(z))
    print(pwd)
    print()
    dictionary = {username, pwd}
    print(dictionary)
    return pwd

def caeser_cipher():
    global super_secret
    super_secret = input('ENTER THE MESSAGE: ')
    global str1
    str1 = ''
    lst = []
    lst = list(super_secret)
    #print(lst)
    for x in lst:
        y = ord(x)
        if y >=48 and y <=57:
            y+=3
        else:
            y +=2
        str1 += chr(y)
    #print(lst)
    print(str1)
    return lst
def decryption():
    key = input('Enter the decryption key: ')
    if key == pwd:
        str2 = ''
        lst2 = []
        lst2 = list(str1)
        for x in lst2:
            y = ord(x)
            if y >=48 and y <=57:
                y-=3
            else:
                y -=2
            str2 += chr(y)
        print(f'Decrypted sentence: {str2}')
    return lst2
while True:
    choice = int(input("Enter '1' for a random password.\nEnter '2' for encryption of a message.\nEnter '3' for decryption.\nEnter '4' to exit: "))
    if choice == 1:
        randpass()
    elif choice == 2:
        caeser_cipher()
    elif choice == 3:
        decryption()
    elif choice == 4:
        break
    else:
        print('Try again')
    
