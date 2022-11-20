import random
import socket

server = socket.socket()
PORT = 55012
maxConn = 1
IP = socket.gethostname()

server.bind((IP, PORT))
server.listen(maxConn)

client, address = server.accept()

"""
quit_info = 0
running = True
try:
    client.send("ready".encode())
except:
    quit_info = 1
    running = False
"""

file = open("wordlist.txt","r")
file_content = file.read()
content_list = file_content.split('\n')
to_guess = random.choice(content_list)

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
    return feedback

user_input = None

while user_input != to_guess and user_input != "quit\n":
    user_input = input("Give Input: ")
    user_input = user_input.strip()
    user_input = user_input.upper()
    while user_input not in content_list and user_input != '1' and user_input != '2':
        user_input = input("Input gresit, da alt input: ")
        user_input = user_input.upper()
        user_input = user_input.strip()

    if user_input == '1':
        client.send('1'.encode())
        next_guess = client.recv(5).decode()
        feedback = give_feedback(to_guess, next_guess)
        client.send(feedback.encode())
        user_input = next_guess
        print(next_guess)
        print(feedback)
    elif user_input == '2':
        while user_input != to_guess:
            client.send('1'.encode())
            next_guess = client.recv(5).decode()
            feedback = give_feedback(to_guess, next_guess)
            client.send(feedback.encode())
            user_input = next_guess
            print(next_guess)
            print(feedback)
    else:
        feedback = give_feedback(to_guess, user_input)
        client.send(user_input.encode())
        client.send(feedback.encode())
        print(feedback)
client.send('quit'.encode())
