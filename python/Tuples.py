import random

vnum = []
for x in range(1050):
    vnumber = random.randint(0, 1050)
    if vnumber not in vnum:
        vnum.append(vnumber)
cand_lst = []
percentages = {}
candidate_list = {}
lst = []
voter_number_storage = []
abstain_storage = []
winning_lst = []
for classes in range(30):
    tutor_grp = input("Enter name of the tutor group: ")
    students = int(input("Enter number of students in the tutor group: "))
    candidates = int(input("Enter number of candidates(MAX 4): "))
    count = 0
    cand1 = 0
    cand2 = 0
    cand3 = 0
    cand4 = 0
    for i in range(candidates):
        candidate_name = input("Enter name of candidate: ")
        cand_lst.append(candidate_name)

    for votes in range(students):
        voter_number = int(input("Enter your unique voter number(between0-1050): "))
        if voter_number in vnum and voter_number not in voter_number_storage:
            choice = input("Enter (vote) to vote and (abstain) to abstain from voting: ")
            if choice.lower() == "vote":
                vote = input(f"Enter candidate name: ")
                if vote == cand_lst[0]:
                    cand1 += 1
                    candidate_list['vote'] = cand1
                elif vote == cand_lst[1]:
                    cand2 += 1
                    candidate_list['vote'] = cand2
                elif vote == cand_lst[2]:
                    cand3 += 1
                    candidate_list['vote'] = cand3
                else:
                    cand4 += 1
                    candidate_list['vote'] = cand4

                candidate_list['vote'] = votes
                # lst.append(candidate_list)
                voter_number_storage.append(voter_number)
                print("Thanks for voting")
            elif choice.lower() == "abstain":
                abstain_storage.append(voter_number)
                print("Thank you!")
                count += 1


        else:
                print("Either wrong input or already voted!")

p = winning_lst.max()
                # win_cand = winning
for k in lst:
    final_no = students - count
    percentage = lst[k] * 100 / (final_no)
    percentages[lst[k]] = percentage
    winning_lst.append([percentages][lst][k])
print('winning candidate is: ', list(percentages.keys())
[list(percentages.values()).index(p)])


