original_lst = []
lst=[]
n = int(input("Enter number of elements to add in the list: "))
for i in range (n):
    elem = input("Enter element: ")
    original_lst.append(elem)
    lst.append(elem)
flag = 0
print('''L I S T   M A N I P U L A T I O N
1) Append an element
2) Insert an element
3) Append a list to the given list
4) Modify an existing element
5) Delete an existing element from its position
6) Delete an existing element with a given value
7) Sort the list in ascending order
8) Sort the list in descending order
9) Display the list.
10) Exit
      ''')
if flag == 0:
    choice = int(input("Enter choice to run the corresponding command: "))
    while choice != 10:
        if choice == 1:
            app_elem = input("enter element to append: ")
            lst.append(app_elem)
            print("List before appending: ", original_lst)
            print("List after appending: ", lst)
        elif choice == 2:
            print("gg")
