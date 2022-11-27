import random

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))
print(x)

# cuvantul citit de la tastatura 
cuv=input("cuv=")

#lista initiata cu valoare vida
s=" "

#Program pentru feedbackul cuvantului cuvantului
for i in range (0,5): 
    if cuv[i]==x[i]:
        #print(2)
        s+="2"+""
    else:    
        if cuv[i] in x:
            #print(1)
            s+="1"+""
        else:
            #print(0)
           s+="0"+""
print(s)