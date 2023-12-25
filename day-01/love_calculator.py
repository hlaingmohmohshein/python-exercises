print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").lower() # What is your name?
name2 = input("What is your beloved one's name? ").lower() # What is their name?
combine_names = name1+ name2
t= combine_names.count('t')
r= combine_names.count('r')
u= combine_names.count('u')
e= combine_names.count('e')
l= combine_names.count('l')
o= combine_names.count('o')
v= combine_names.count('v')
true = t+r+u+e
love = l+o+v+e
total = int(str(true)+ str(love))
mark =true+love
if mark< 10 or mark>90:
   print(f"Your score is {total}, you go together like coke and mentos.")
elif mark>40 or mark> 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}")
