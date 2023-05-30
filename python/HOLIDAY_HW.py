# n = int(input("no. of elements: "))
# for i in range(n):
#     e = input("Enter the elements: ")
#     list = [e]
#     print(list)
# f = input("Enter the element to search: ")
# g = (list.index(f))
# print(g)
# wronggg

# list = []
# e = input("Would you like to input (numbers) as elements or (strings)?: ")
# if e == "numbers":
#     print("Enter elements to add in the list: ")
#     for i in range(5):
#         value = int(input())
#         list.append(value)
#     print("Enter an element to search in the created list: ")
#     element = int(input())
#     for i in range(5):
#         if element == list[i]:
#             print("Element is at Index:", i)
#             print("Element is at Position:", i+1)
# else:
#     print("Enter elements to add in the list: ")
#     for i in range(5):
#         value = (input())
#         list.append(value)
#     print("Enter an element to search in the created list: ")
#     element = (input())
#     for i in range(5):
#         if element == list[i]:
#             print("Element found at Index:", i)
#             print("Element found at Position:", i+1)
# OH YEASSS I DID IT

list = []
e = input("Would you like to input (numbers) as elements or (strings)?: ")
n = int(input("Enter number of elements to add in the list: "))
if e == "numbers":
    print("Enter elements to add in the list: ")
    for i in range(n):
        value = int(input())
        list.append(value)
    print("Enter an element to search in the created list: ")
    element = int(input())
    for i in range(n):
        if element == list[i]:
            print("Element is at Index:", i)
            print("Element is at Position:", i+1)
else:
    print("Enter elements to add in the list: ")
    for i in range(n):
        value = (input())
        list.append(value)
    print("Enter an element to search in the created list: ")
    element = (input())
    for i in range(n):
        if element == list[i]:
            print("Element found at Index:", i)
            print("Element found at Position:", i+1)
