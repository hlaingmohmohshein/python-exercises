import random
word_list = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_lenght = int(len(chosen_word))
display = []
end_of_game= False
for chose_letter in chosen_word:
    display.append("_")
while end_of_game ==False:  
    guess = input("Guess Letter!")
    for position in range(word_lenght):
        letter = chosen_word[position]
        if guess == letter:
            display[position]=letter
    print(display)        
    if "_" not in  display:
        end_of_game = True   
        print('You Win. Congratulations!')    
