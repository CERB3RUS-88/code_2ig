# # import mysql.connector as msq
# # db = msq.connect(
# #     host = "localhost",
# #     user = "root",
# #     password = "root",
# #     database = "project"
# # )
# # mycursor = db.cursor()
# # mycursor.execute("select * from  student")
# # for i in mycursor:
# #     print(i)


# while True:
#     try:
#         accnum=int(input("Account number: "))
#         break
#     except Exception as e:
#         print("Please enter a valid account number.")
# while len(str(accnum))!=9:
#     print("Please enter a valid account number.")
#     accnum=int(input("Account number: "))
#     if len(str(accnum))==9:
#         break
che=True
while che==True:
    try:
        accnum=int(input("Account number:"))
        che=False
        break
    except Exception:
        print("Please enter a valid account number.")
        che=True
while len(str(accnum))!=9:
    print("Please enter a valid account number.")
    accnum=int(input("Account number:"))
    if len(str(accnum))==9:
        break