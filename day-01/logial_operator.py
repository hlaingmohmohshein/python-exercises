print("Welcome to the rollercoaster!")
height= int(input("What's your height in cm ?"))
bill = 0
if height > 120:
    print("You can ride the rollercoaster!")
    age = int(input("How old are you ? "))
    if age < 12:
        print("Childred tickets are $5.'")
        bill+= 5
    elif age >=12 and age <18:
        print("Youth tickets are $7.'")
        bill+=7
    elif age>=18:
        print("Adult tickets are $12.'")
        bill+=12
    elif age> 45 and age< 55:
        print("Everything is going to be OK. Have a free ride on us!'")
        bill+=0
    wants_photo= input("Wants photo . Y or N ?")
    if wants_photo== 'Y':
        bill+=3
    print(f"Your total bill is $ {bill}")
else:
    print("You cannot ride the rollercoaster!")
