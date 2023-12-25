print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
small_size_bill = 15
medium_size_bill = 20
large_size_bill = 25
bill=0
if size == 'S':
    if add_pepperoni == 'Y' and extra_cheese =='Y': 
        bill =small_size_bill + 2 + 1
    elif add_pepperoni == 'Y' or extra_cheese =='Y':
        if add_pepperoni == 'Y':
            bill =small_size_bill + 2
        elif extra_cheese =='Y':
            bill =small_size_bill + 1
    else:
        bill =small_size_bill
elif size == 'M':
    if add_pepperoni == 'Y' and extra_cheese =='Y': 
        bill =medium_size_bill + 3 + 1
    elif add_pepperoni == 'Y' or extra_cheese =='Y':
        if add_pepperoni == 'Y':
            bill =medium_size_bill + 3
        elif extra_cheese =='Y':
            bill =medium_size_bill + 1
    else:
        bill =medium_size_bill
else:
    if add_pepperoni == 'Y' and extra_cheese =='Y': 
        bill =large_size_bill + 3 + 1
    elif add_pepperoni == 'Y' or extra_cheese =='Y':
        if add_pepperoni == 'Y':
            bill =large_size_bill + 3
        elif extra_cheese =='Y':
            bill =large_size_bill + 1
    else:
        bill =large_size_bill
print(f"Your final bill is: ${bill}.")   
