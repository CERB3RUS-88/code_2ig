student_names = []
student_marks = []

# Collect student names and marks
for i in range(5):
    student_name = input(f"Enter the name of student {i + 1}: ")
    student_names.append(student_name)

    marks = []
    for j in range(3):
        subject_name = input(f"Enter the marks for {student_name} in subject {j + 1}: ")
        marks.append(float(subject_name))

    student_marks.append(marks)

# Display the data in a tabular form
print("\nStudent Report")
print("-" * 34)
print(f"{'Name':<15}{'Subject 1':<10}{'Subject 2':<10}{'Subject 3':<10}")
print("-" * 34)

for i in range(5):
    print(f"{student_names[i]:<15}", end="")
    for j in range(3):
        print(f"{student_marks[i][j]:<10.2f}", end="")
    print()









#number = int(input ("Enter the number of which the user wants to print the multiplication table: "))      
# We are using "for loop" to iterate the multiplication 10 times       
#print ("The Multiplication Table of: ", number)    
#for count in range(1, 11):      
#   print (number, 'x', count, '=', number * count, end='\n')    
