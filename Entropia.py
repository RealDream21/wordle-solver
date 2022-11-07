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

block=[0 for i in range(242)]
word_tryout="ABACA"
entropia=0.0
for template in B3:
    
    poz=0
    
    copy_list=content_list[:]

    litera_blocata=[0 for i in range(25)] #practic aici pun de cate ori imi apare litera in cuvant 
                                          #in functie de cati de 1 si 2 am
    
    for letter in range (5):    
        if template[letter]==2: 
            litera_blocata[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cresc aparatiile
            
    for letter in range (5):    
        if template[letter]==1: 
            litera_blocata[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cresc aparitiile

    while poz < len (content_list):

        aparitii_lit_cuv_lista=[0 for i in range(25)] #aparitiile literei cuvantului din listap
        
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
            
            for letter in range (5):
                if template[letter]==1:
                    litera_blocata[ord(word_tryout[letter])-ord('A')] 
            
            for letter in range (5):
                if template[letter]==0 and litera_blocata[ord(word_tryout[letter])-ord('A')]==0:
                    if word_tryout[letter] in content_list[poz]:
                        block[poz]=1
                elif template[letter]==0 and litera_blocata[ord(word_tryout[letter])-ord('A')]!=0:
                
            
        poz=poz+1
    #entropia+=entropy(nr_cuv_elim)
#print (entropia)


#ceva ifuri
""" elif template[letter]==1:
                if word_tryout[letter] in content_list[poz] and word_tryout[letter]!=content_list[poz][letter]:
                    block[poz]=1  
            elif template[letter]==0:
                if word_tryout[letter] in content_list[poz]:
                    block[poz]=1"""


"""

daca e 0 consider ca nu exista
dar e posibil sa am
ABACA
22200

si cuv ABBBB

deci eu trebuie sa verific daca mai sunt de 2 sau 1 si e aceeasi litera cu litera care are 0 in template



"""


"""
B3_v2=[]
for i in range(243):
    aux=i
    text =""
    for j in range(5):
        text = text + str(aux % 3)
        aux=aux//3
    B3_v2.append(text)
sum_entropy = 0
word = "ABACA"
for template in B3_v2:
    nr_cuv_eliminate = 0
    for tryout_word in content_list:
        elim = 0
        for index in range(5):
            if template[index] == "2" and tryout_word[index] != word[index]:
                elim = 1
            elif template[index] == "1" and word[index] not in tryout_word:
                elim = 1
        nr_cuv_eliminate += elim
    sum_entropy += entropy(nr_cuv_eliminate)
print(sum_entropy)
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

#program
"""

nr de cuv eliminat
suma de len()-nr de cuv eliminat 
salvam cuvant cu entropia cea mai mare
vrei sa ramai in lista cu cuvintele ramase DUPA ce primesti 
feeedback de la primu program, 

eliminarea din lista tot in primu

"""


poz=0
while poz < len(content_list):
    cuv=content_list[poz]
    for i in range (poz):
        cuvanalizat=content_list[i]
    poz=poz+1
    


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

#afisare
g = open('data.out.txt','w')
#g.write(x)
f.close
g.close

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
