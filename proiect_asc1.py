import random

#citire si crearea listei
f = open('wordlist.txt','r')

#luam un cuvant random
x = random.choice(list(f))

#afisare
g = open('data.out','w')
print (x)
g.write(x)
f.close
g.close
