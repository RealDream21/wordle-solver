import random
from re import S

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))

# numar citit de la tastatura 
nr=input("nr=")

# lista initiata cu valoare vida
s=" "

# Program pentru ghcirea cuvantului
for i in range (0,5):
        if nr[i]==x[i]:
            #print(2)
            s+=x[i]+""
        else:    
            if nr[i] in x:
                #print(1)
                s+="1"+""
            else:
                #print(0)
               s+="0"+""
print(s)


#afisare
g = open('data.out','w')
print (x)
g.write(x)
f.close
g.close

#COMPARA CU ALA DE JOS 