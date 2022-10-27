import random

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))

nr=input("nr=")
#Program pentru ghcirea cuvantului
for i in range (0,len(nr)):
        if nr[i]==x[i]:
            print(2)
        else:    
            if nr[i] in x:
                print(1)
            else:
                print(0)


#afisare
g = open('data.out','w')
print (x)
g.write(x)
f.close
g.close

