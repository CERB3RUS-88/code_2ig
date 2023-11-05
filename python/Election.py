import random
vnum = []
for x in range(1050):
    vnumber = random.randint(0,1050)
    if vnumber not in vnum:
        vnum.append(vnumber)
    

candidate_list = {}
lst = []
voter_number_storage = []
abstain_storage = []
for classes in range(30):
    tutor_grp = input("Enter name of the tutor group: ")
    students = int(input("Enter number of students in the tutor group: "))
    candidates = int(input("Enter number of candidates(MAX 4): "))
    for i in range (candidates):
        candidate_name = input("Enter name of candidate: ")
    for votes in range(students):
        voter_number = int(input("Enter your unique voter number(between0-1050): "))
        if voter_number in vnum and voter_number not in voter_number_storage:
            choice = input("Enter (vote) to vote and (abstain) to abstain from voting: ")
            if choice.lower() == "vote":
                vote = input(f"Enter candidate name: ")
                candidate_list = {vote:votes}
                lst.append(candidate_list)
                voter_number_storage.append(voter_number)
                print("Thanks for voting")
            elif choice.lower() == "abstain":
                abstain_storage.append(voter_number)
                print("Thank you!")
        else:
            print("Either wrong input or already voted!")

                



