#date = int(input("Enter date: "))
#month = input("Enter month: ")
year = int(input("Enter Year: "))
sum1 = 0
sum2 = 0
for i in range(year,2023):
    if i%4 == 0:
        sum1+=366
    else:
        sum2+=365
total_sum = sum1+sum2
print(total_sum)

