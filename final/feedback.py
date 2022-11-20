import random

file = open("wordlist.txt","r")
to_guess = random.choice(list(file))
user_input = input("Give Input: ")

def give_feedback(guess, input):
    feedback = ""
    for i in range (0, 5):
        if input[i] == guess[i]:
            feedback += "2"
        else:
            if input[i] in guess:
                feedback += "1"
            else:
                feedback += "0"
    return [feedback, input]
