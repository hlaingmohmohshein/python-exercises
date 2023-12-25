pi = 3.14159246
total_even_number=0
even_number_range =int(input('Number Range'))
for number in range(2,even_number_range,2):
    if number%2 ==0:
        total_even_number += number
print(total_even_number)
