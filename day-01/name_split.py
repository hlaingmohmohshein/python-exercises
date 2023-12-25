import random
names_string = 'A','B','Hlaing MOh Moh Shein','Htet Wai Yan','Aung Thuta Myat','Cho Cho Oo','Thi Thi MOe'
names = names_string.split(',')
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
length = len(names)
random_number = random.randint(0,length-1)
print(f"{names[random_number]} is going to buy the meal today!")