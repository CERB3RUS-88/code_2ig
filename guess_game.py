secret_number = 8
guess_count = 0
guess_limit = 3
print("You have 3 guesses can you guess the secret number which is between 0 and 10")
while guess_count < guess_limit:
    guess = int(input('guess:  '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print("Sorry you lost!")
