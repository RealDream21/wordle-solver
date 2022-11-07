import random
import math

f = open('wordlist.txt','r')

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

#creez matrice cu toate posibilitatile in baza 3
B3=[]
for i in range(243):
    aux=i
    Linie=[]
    for j in range(5):
        Linie.append(aux%3)
        aux=aux//3
    B3.append(Linie)

#am afisat matricea

"""

g = open('template.txt','w')
for line in B3:
    for column in line:
        g.write(str(column))
    g.write('\n')

"""

#entropia
def entropy(nr_cuvinte_eliminate):
    cuv_totale=len(content_list)
    numarator = cuv_totale - nr_cuvinte_eliminate
    #print(numarator, nr_cuvinte_eliminate, cuv_totale, sep=" ")
    shanon = (numarator/cuv_totale)*(math.log2((cuv_totale/numarator)))
    return shanon

"""
for word in content_list:
    nr_cuv_elim=0
    test_list = content_list.copy()
    for template in B3:
        for letter, value, index in zip(word, template, range(5)):
            for word_tryout in content_list:
                if value==2 and word_tryout[index] != letter:
                    nr_cuv_elim+=1
                elif value == 1 and letter not in word_tryout:
                    nr_cuv_elim+=1
                elif value == 0 and letter in word_tryout:
                    nr_cuv_elim+=1

"""

#AIIIICI

g = open('data.out.txt','w')

block=[0 for i in range(len(content_list))]
litera_blocata=[0 for i in range(26)] #practic aici pun de cate ori imi apare litera in cuvant 
                                      #in functie de cati de 1 si 2 am

word_tryout="ABACA"
entropia=0.0
for template in B3:
    for i in range(len(content_list)):
        block[i]=0

    g.write(word_tryout)
    g.write('\n')
    g.write(str(template))
    g.write('\n')
    g.write('\n')

    poz=0
    
    #copy_list=content_list[:]

    for i in range(26):
        litera_blocata[i]=0
    
    for letter in range (5):    
        if template[letter]==2:
            litera_blocata[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cresc aparatiile
            
    for letter in range (5):    
        if template[letter]==1: 
            litera_blocata[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cresc aparitiile

    while poz < len (content_list):

        aparitii_lit_cuv_lista=[0 for i in range(26)] #aparitiile literei cuvantului din lista
        
        for letter in range (5):
            aparitii_lit_cuv_lista[ord(content_list[poz][letter])-ord('A')]+=1

        for letter in range (5):
            if litera_blocata[ord(word_tryout[letter])-ord('A')]!=0: #daca litera mea exista in cuvant, adica am cel putin o val de 1 sau de 2 atunci ma uit in cuvantul meu
                for letter_sec in range(5):
                        if word_tryout[letter]==content_list[poz][letter_sec]: #daca litera mea e in cuv atunci verific daca imi apare de mai multe ori sau nu
                            if litera_blocata[ord(word_tryout[letter])-ord('A')]>aparitii_lit_cuv_lista[ord(content_list[poz][letter_sec])-ord('A')]:    
                                block[poz]=1 # daca litera mea apare de mai multe ori decat in cuvant atunci elimin cuvantul ca nu e posibil sa primesc tipul ala de feedback pe el
        
        if block[poz]==0:
            for letter in range (5):
                if template[letter]==2: 
                    if word_tryout[letter]!=content_list[poz][letter]:
                        block[poz]=1
            
        if block[poz]==0:
            for letter in range (5):
                if template[letter]==1: #daca am 1 tre neaparat sa fie in cuvant
                    if word_tryout[letter]==content_list[poz][letter]:
                        block[poz]=1
                    if word_tryout[letter] not in content_list[poz]: 
                        block[poz]=1

        if block[poz]==0:
            for letter in range (5):
                if template[letter]==0 and litera_blocata[ord(word_tryout[letter])-ord('A')]==0:
                    if word_tryout[letter] in content_list[poz]:
                        g.write(content_list[poz])
                        g.write('\n')
                        block[poz]=1 
                   
        poz=poz+1
    g.write('\n')  
    g.write("Cuvinte care raman:\n")

    """
    for i in range (len(content_list)):
        if block[i]==0:
            g.write(content_list[i])
            g.write('\n')
    """
    
    # numaram cuvintele eliminate   
    nr_cuv_elim=0
    for i in range (len(content_list)):
        if block[i]==0:
            g.write(content_list[i])
            g.write('\n')

    for i in range (len(content_list)):
        if block[i]==1:
            nr_cuv_elim+=1

    g.write('\n')

    #calculam entropia
    entropia+=entropy(nr_cuv_elim)

print (entropia)

g.close()

"""

OBSERV CA NU RAMAN DOAR CUVINTELE CARE CONTIN LITERA CU VAL 1


daca e 0 consider ca nu exista
dar e posibil sa am
 A  B  A  C  A
[1, 1, 0, 1, 0]
[0, 1, 1, 1, 0]
[0, 1, 0, 1, 1]



si cuv ABBBB

deci eu trebuie sa verific daca mai sunt de 2 sau 1 si e aceeasi litera cu litera care are 0 in template

"""

"""
ABACA
00000
00001   cuv[4]!=cuv_content[4] and cuv[4] in cuv_content
00002
00010
00011
00012
00020
00022
suma de pi*log2(pi)
pi=cuvramase/len(content_list)

"""

"""
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

"""
#afisare
g = open('data.out.txt','w')
#g.write(x)
f.close
g.close
"""

"""
for i in range (5):
    ap[ord(x[i])-ord("A")]+=1
    
    
for ...    
    if cuv[i]==x[i]:
        s=s+x[i]+""
        ap[ord(x[i])-ord("A")]-=1
    elif x[i] in cuv and ap[ord(x[i])-ord("A")]>0:
        s+="1"+""
"""
