import random
def votenumber_generation():
    vnum = []
    for x in range(1050):
        vnumber = random.randint(0,1050)
        if vnumber not in vnum:
            vnum.append(vnumber)
    for votes in range(students):
                voter_number = int(input("Enter your unique voter number(between0-1050): "))
                if voter_number in vnum:
                    votes = input(f"Enter vote of student{votes+1}: ")
                    candidate_list = {candidate_name:votes}

def voting():
    candidate_list = {}
    for classes in range(30):
        tutor_grp = input("Enter name of the tutor group: ")
        students = int(input("Enter number of students in the tutor group: "))
        candidates = int(input("Enter number of candidates(MAX 4): "))
        for i in range (candidates):
            candidate_name = input("Enter name of candidate: ")
            votenumber_generation()
            '''
            for votes in range(students):
                voter_number = int(input("Enter your unique voter number(between0-1050): "))
                if voter_number in vnum:
                    
                
                votes = input(f"Enter vote of student{votes+1}: ")
                candidate_list = {candidate_name:votes}
'''


