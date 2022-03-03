currency = int(input('enter the currency:  '))

unit = input('(R)upees or (P)aise: ')

if unit.upper() == "R":

    converted_currency = currency * 100

    print(f"It is {converted_currency} paise")

else:

    converted_currency = currency / 100

    print(f"It is {converted_currency} rupees")
