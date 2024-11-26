sentence1 = input("Enter 1st sentence: ")
sentence2 = input("Enter 2nd sentence: ")
with open('hello_Test_file.txt','w') as f:
    f.write(sentence1+"\n")
    f.write(sentence2)
def check_uppercase():
    lst = []
    c = 0
    with open('hello_Test_file.txt', 'r') as f:
        for line in f:
            w = line.split()
            lst.append(w)
        # print(lst)
        for x in lst:
            # print(f"x is {x}")
            for y in x:
                # print(f"y is {y}")
                if y.isupper():
                    c+=1
    print(f"Upper case: {c}")
def check_lowercase():
    lst = []
    c = 0
    with open('hello_Test_file.txt', 'r') as f:
        for line in f:
            w = line.split()
            lst.append(w)
        # print(lst)
        for x in lst:
            # print(f"x is {x}")
            for y in x:
                # print(f"y is {y}")
                if y.islower():
                    c+=1
    print(f"Lower case: {c}")
def check_title():
    lst = []
    c = 0
    with open('hello_Test_file.txt', 'r') as f:
        for line in f:
            w = line.split()
            lst.append(w)
        # print(lst)
        for x in lst:
            # print(f"x is {x}")
            for y in x:
                # print(f"y is {y}")
                if y.istitle():
                    c+=1
    print(f"First letter capital case: {c}")
check_uppercase()
check_lowercase()
check_title()
