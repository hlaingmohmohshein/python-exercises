import random
#Step 1
word_list = ["ardvark","baboon","camel"]
#TODO-1- Randomly choose a word form the word_list and assign it to a variabel name called choose_list
chosen_word = random.choice(word_list)
print(chosen_word)
hint_chosen_word = []
for count in range(len(chosen_word)):
    hint_chosen_word.append('_')
print(f"Chosen word is as like this !\n {hint_chosen_word}")
#TOD0-2- Ask the user to guess a letter and assign their answer to a variable called guess. Make guess to lowercase.
guess = input("Guess a letter! ").lower()
#TODO-3- Check if the letter the user gussed (guess) is one of the letters in the chosen_word.
#For each letter chosen_word, add a "_" to display
#So if the chosen word is "Apple", display should be ['_','_','_','_','_'] wiht 5 "_" respresenting each letter to guess.
guess_outcame= []
for letter in chosen_word:
    if guess == letter:
        guess_outcame.append(guess)  
    else:
       guess_outcame.append('-')
print(guess_outcame)
