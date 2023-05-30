# # # ques 1
# # alpha = input("Enter the character: ")
# # if alpha == ("a") or alpha == ("e") or alpha == ("i") or alpha == ("o") or alpha == ("u") or alpha == ("A") or alpha == ("E") or alpha == ("I") or alpha == ("O") or alpha == ("U"):
# #     print("It's a vowel")
# # else:
# #     print("It's a consonant")


# # ques 2
# integer = int(input("Enter the integer: "))
# if integer % 5 == 0 and integer % 7 == 0:
#     print("It is the multiple of both 5 and 7")
# else:
#     print("It is not the multiple of both 5 and 7")

# # ques 3
# list = [1, 2, 3, 4, 5]
# print(list)
# list[0], list[-1] = list[-1], list[0]
# print(list)


# Ques 4

# subjects = ["Math", "English", "Science", 'Hindi', 'Social Science']
# print(subjects)
# sixth_subject = (input("Enter 6th subject: "))
# subjects.append(sixth_subject)
# print(subjects)
# subjects[0], subjects[2] = subjects[2], subjects[0]
# print(subjects)
# subjects.pop(3)
# print(subjects)

# Ques 5
item_code = int(input("Enter the item item_code: "))
if item_code == 100:
    print("The discount on Refrigerator is 10%")
elif item_code == 101:
    print("The discount on Smart TV is 20%")
elif item_code == 102:
    print("The discount on Microwave oven is 5%")
elif item_code == 103:
    print("The discount on Laptop is 12%")
