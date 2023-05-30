rows = int(input("How many rows: "))
coloums = int(input("How many coloumns: "))
symbol = (input("Enter a symbol to use: "))

for i in range(rows):
    for j in range(coloums):
        print(symbol, end="")
    print()
