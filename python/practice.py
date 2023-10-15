# player1 = 0
# player2 = 0
# count = 0


# for i in range(5):
#     coin = int(input("Enter the number (1)(2): "))
#     if coin == 1:
#         player1 += 1
#         count += 1
#     elif coin == 2:
#         player2 += 1
#         count += 1
# if player1 > 2:
#     print("Player 1 wins!")
# else:
#     print("Player 2 wins!")

# imp function

# prompt = "print all multiples of 5"
# num1 = int(input(prompt))
num = 1
while num < 25:

    product = 5*num
    print(product)
    num += 1
    if product == 25:
        break
    else:
        continue
