#take names of 5 students and then input marks of 5 subjects of all 5 students then display
lst=[]
for w in range(5):
    names = input(f"enter names of student{w+1}: ")
    lst.append(names)
print("enter marks of maths, physics, chemistry, english, cs in order of all 5 students")
for x in range(5):
    

#    for y in range(5):
#        marks = float(input(f"enter marks of student {x+1} in subject {y+1}:  "))

#        mydict = {names: marks}
#        print(mydict)
#        print(names, " ", marks, end='\n') 