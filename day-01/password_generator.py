import random
print("Welcome to the password Generator!")
letters= int(input("How many letters would you like in your passwords?"))
symbos= int(input("How many symbols would you like?"))
numbers=int(input("How many number would you like?"))
letters_list =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',  'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symble_lists = ['@','_','!','#','$','%','^','&','*']

pass_letter= ''
for letter in range(1,letters+1):
    pass_letter += random.choice(letters_list).append()
for number in range(1,numbers+1):
    pass_letter +=str(number)
for number in range(1,symbos+1):
    pass_letter += random.choice(symble_lists)

# print(random.shuffle(pass_letter))