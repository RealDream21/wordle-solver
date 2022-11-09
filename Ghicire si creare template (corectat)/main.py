import random

file = open("wordlist.txt")
lines = file.readlines()

guess = "TARAE"
#guess = guess[:(len(guess) - 1)]
myInput = input("Input word: ")

feedback = "00000"
guess_list = list(guess)
feedback = list(feedback)
for i in range(5):
    if myInput[i] == guess[i]:
        feedback[i] = "2"
        guess_list[i] = "0"
for i in range(5):
    if feedback[i] == "0":
        index = None
        try:
            index = guess_list.index(myInput[i])
        except:
            pass
        else:
            guess_list[index] = "0"
            feedback[i] = "1"
print()
print(myInput)
print(guess)
print("".join(feedback))