import random
#salut
#salut2
#citire si crearea listei
f = open('wordlist.txt','r')

"""
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
print (x)
g.write(x)
f.close
g.close
"""

#afisare
g = open('data.out','w')
print (len(content_list))
g.write(x)
f.close
g.close


#COMPARA CU ALA DE JOS 