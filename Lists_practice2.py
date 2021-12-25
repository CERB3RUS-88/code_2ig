mark1 = int(input("Enter the marks of student 1: "))
mark2 = int(input("Enter the marks of student 2: "))
mark3 = int(input("Enter the marks of student 3: "))
mark4 = int(input("Enter the marks of student 4: "))
mark5 = int(input("Enter the marks of student 5: "))
mark6 = int(input("Enter the marks of student 6: "))


marks_list = [mark1, mark2, mark3, mark4, mark5, mark6]

marks_list.sort()

print(f"The sorted list of marks is {marks_list}")
