n = input("Enter a string: ")
mid_String = input("enter mid string: ")
lst = n.split()
middle = len(lst)//2 
k = lst[0:middle] + [mid_String] + lst[middle:]
k = ' '.join(k)
print(k)