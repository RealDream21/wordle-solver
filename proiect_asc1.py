import random

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))

# cuvantul citit de la tastatura 
cuv=input("cuv=")

#lista initiata cu valoare vida
s=" "

#Program pentru ghcirea cuvantului
for i in range (0,5): 
    if cuv[i]==x[i]:
        #print(2)
        s+=x[i]+""
    else:    
        if cuv[i] in x:
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