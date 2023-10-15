# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# num3 = [7, 8, 9]
# print(num1)
# num = [num1, num2, num3]
# print(num[0][1])
# num_lists = int(input("How many lists do you want? "))
# lists = []
# for p in range(num_lists):
#     x = int(input("enter number : "))
#     lists.append([x])
lists = int(input("How many lists do you want? "))
varname = 'list'
for i in range(lists):
    exec(f"{varname}{i} = []")
exec(f'print(f"list{lists-1} is", list{lists-1})')
