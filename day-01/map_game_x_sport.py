line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
# A1
line1 = ["1","️2","️3"]
line2 = ["4","5","️6"]
line3 = ["7","8","9"]
row_list = ['A','B','C']
line_list= [line1,line2,line3]
col = position[0]
row=  int(position[1])
# B2
B=row_list.index(col)
print(B)
print(line1[B][row-1])
if col == 'A':
    line1[B][row-1]="X"
elif col == 'B':
    line2[B][row-1]="X"
elif col == 'C':
    line3[B][row-1]="X"
# list[1][1]='X'
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")
