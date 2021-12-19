Student_Names = ['Shaurya', 'Monty', 'Pratham', 'Aryan',
                 'Harshil', 'Anikesh', 'Shashwat', 'Shreyas', 'Tanishq', 'Mona']
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Changing the value at index 2
Student_Names[2] = 'Pappu'
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Adding an element at the end of the list
Student_Names.append("Pratyay")
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Inserting an element at index 4
Student_Names.insert(4, "Syed")
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Removing an element
Student_Names.remove("Monty")
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Removing an element using index
Student_Names.pop(-2)
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# deleting an element using index(same as pop with a different syntax)
del Student_Names[-3]
print(Student_Names)
print(len(Student_Names))
print("                                              ")

# Sorts the list
ss = sorted(Student_Names)
print(ss)

print("                                              ")

# Multiplies the list i.e repeating it
gg = Student_Names * 2
print(gg)

print("                                              ")

# Creating another list
List = ["Orange", "Banana"]

print("                                              ")

# Combining the lists
combined_list = Student_Names + List
print(combined_list)
