import random
#salut
#salut2
#citire si crearea listei
f = open('wordlist.txt','r')

"""
#luam un cuvant random
x = random.choice(list(f))
x = x[:(len(x)-1)]
# cuvantul citit de la tastatura 
cuv=input("cuv=")

#Sir initiat cu valoare vida
s="00000"
#lista de litere 
guess_list=list(x)
s=list(s)
#Program pentru ghcirea cuvantului
for i in range (0,5):
    if cuv[i]==x[i]:
        s[i]=x[i]
        guess_list[i]="0"
for i in range (0,5):
    if s[i]=="0":
        try:
           guess_list.index(cuv[i])
        except:
            pass
        else:
<<<<<<< HEAD
            s[i]="1"
print(x)
print(cuv)
print("".join(s))
=======
            #print(0)
           s+="0"+""
print(s)
"""

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

#luam un cuvant random
x = random.choice(content_list)

#sterge elementele din lista care au o literea din cuv
cuv="ROITE"
poz=0
while poz < len(content_list):
    if cuv[0] in content_list[poz]: 
        del content_list[poz]
        poz=poz-1
    poz=poz+1    
>>>>>>> main

"""
#afisare
g = open('data.out','w')
g.write(x)
f.close
g.close
"""

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
"""

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

#luam un cuvant random
x = random.choice(content_list)

#sterge elementele din lista care au o literea din cuv
cuv="ROITE"
poz=0
while poz < len(content_list):
    if cuv[0] in content_list[poz]: 
        del content_list[poz]
        poz=poz-1
    poz=poz+1    

"""
#afisare
g = open('data.out','w')
print (len(content_list))
g.write(x)
f.close
g.close
<<<<<<< Updated upstream
"""

#afisare
g = open('data.out','w')
print (len(content_list))
g.write(x)
f.close
g.close
=======
>>>>>>> Stashed changes


#COMPARA CU ALA DE JOS 