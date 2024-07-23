# def is_leap(year):
#     leap = False

#     # Write your logic here
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 leap = True
#             else:
#                 leap = False
#         else:
#             leap = True
#     else:
#         leap = False

#     return leap


# year = int(input())
# print(is_leap(year))

def minion_game(string):
    # your code goes here
    score1 = 0
    score2 = 0
    while True:
        n1 = input("Substring Kevin: ")
        if n1[0] == 'A' or n1[0] == 'E' or n1[0] == 'I' or n1[0] == 'O' or n1[0] == 'U':
            if s.find(n1) != -1:
                a = s.count(n1)
                score1 += a
                continue
            else:
                break
        else:
            break
    while True:
        n2 = input("Substring Stuart: ")
        if n2[0] != 'A' or n2[0] != 'E' or n2[0] != 'I' or n2[0] != 'O' or n2[0] != 'U':
            if s.find(n2) != -1:
                b = s.count(n2)
                score2 += b
                continue
            else:
                break

    if score1 > score2:
        print("Kevin winner, his score is " + str(score1))
    elif score2 > score1:
        print("Stuart Winner, his score is " + str(score2))
    else:
        print("tie")


if __name__ == '__main__':
    s = input()
    minion_game(s)
