import random

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))

# cuvantul citit de la tastatura 
cuv=input("cuv=")

#lista initiata cu valoare vida
s=" "

#contor: de cate ori este litera in cuv
k=0

#Program pentru ghcirea cuvantului
for i in range (0,5): 
    k=x.count(cuv[i])
    print(k)
    if cuv[i]==x[i]:
        #print(2)
        s+=x[i]+""
        k=k-1
    else:    
        if cuv[i] in x:
            #print(1)
            s+="k"+""
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