import math
from tqdm import tqdm

#entropia
def entropy(nr_cazuri_template, modified_content_list):
    cuv_totale=len(modified_content_list)

    shanon = (nr_cazuri_template/cuv_totale)*(math.log2((cuv_totale/nr_cazuri_template)))
    return shanon

#returneaza cuvantul cu cea mai mare entropie
def Word_With_Max_Entropy(modified_content_list):
    
    if (len(modified_content_list)==1):
        return modified_content_list[0]

    freq_template=[0 for i in range(243)]

    templates=[]

    pos_temp=0

    entropy_max=0.0
    word_entropy_max=[""]

    for word in tqdm(modified_content_list): # pt cuvantul asta eu primesc feedback
    
        pos_temp=0
        entropy_calc=0.0

        templates=[]

        for i in range(243):
            freq_template[i]=0
            
        for word_tryout in modified_content_list: #asta e guess
            
            word_try = word
            guess=word_tryout
            feedback = "00000"
            guess_list = list(guess) # lista din literele cuv
            feedback = list(feedback)

            for i in range(5):
                if word_try[i] == guess[i]:
                    feedback[i] = "2"
                    guess_list[i] = "0"

            for i in range(5):
                if feedback[i] == "0":
                    index = None
                    try:
                        index = guess_list.index(word_try[i])
                    except:
                        pass
                    else:
                        guess_list[index] = "0"
                        feedback[i] = "1"
            
            feedback="".join(feedback)

            try:
                pos_temp=templates.index(feedback)
                freq_template[pos_temp]+=1
            except:
                templates.append(feedback)
                freq_template[len(templates)-1]=1

        for i in range(len(templates)):
            entropy_calc+=entropy(freq_template[i], modified_content_list)

        if entropy_calc>entropy_max:
            entropy_max=entropy_calc
            word_entropy_max[0]=word

    return word_entropy_max

#sterg cuvintele care nu imi convin din lista

def delete_from_list(word_tryout, template, list_words):
    
    remaining_words=[]

    #template este string si eu trebuie sa il fac int
    template=[int(x) for x in template]
    print(template)

    block=[0 for i in range(len(list_words))]

    litera_blocata_2=[0 for i in range(26)] #practic aici pun de cate ori imi apare litera in cuvant 
                                        #in functie de cati de 2 am

    litera_blocata_1=[0 for i in range(26)] #practic aici pun de cate ori imi apare litera in cuvant 
                                        #in functie de cati de 1 am

    aparitii_lit_cuv_word_tryout=[0 for i in range(26)]

    aparitii_lit_cuv_lista=[0 for i in range(26)] #aparitiile literei cuvantului din lista

    poz=0
    
    for letter in range (5):
        aparitii_lit_cuv_word_tryout[ord(word_tryout[letter])-ord('A')]+=1

    for letter in range (5):    
        if template[letter]==2:
            litera_blocata_2[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cu temp 2 cresc aparatiile
                
    for letter in range (5):    
        if template[letter]==1: 
            litera_blocata_1[ord(word_tryout[letter])-ord('A')]+=1 #daca litera imi apare in cuvant cu temp 1 cresc aparitiile

    while poz < len (list_words):

        for i in range(26):
            aparitii_lit_cuv_lista[i]=0 #aparitiile literei cuvantului din lista
            
        for letter in range (5):
            aparitii_lit_cuv_lista[ord(list_words[poz][letter])-ord('A')]+=1

        for letter in range (5):
            if litera_blocata_1[ord(word_tryout[letter])-ord('A')]!=0 or litera_blocata_2[ord(word_tryout[letter])-ord('A')]!=0: #daca litera mea exista in cuvant, adica am cel putin o val de 1 sau de 2 atunci ma uit in cuvantul meu
                for letter_sec in range(5):
                        if word_tryout[letter]==list_words[poz][letter_sec]: #daca litera mea e in cuv atunci verific daca imi apare de mai multe ori sau nu
                            if (litera_blocata_1[ord(word_tryout[letter])-ord('A')]+litera_blocata_2[ord(word_tryout[letter])-ord('A')])>aparitii_lit_cuv_lista[ord(list_words[poz][letter_sec])-ord('A')]:    
                                block[poz]=1 # daca litera mea apare de mai multe ori decat in cuvantul incercat, atunci elimin cuvantul din lista ca nu e posibil sa primesc tipul ala de feedback pe el
            
        if block[poz]==0:
            for letter in range (5):
                if template[letter]==2: 
                    if word_tryout[letter]!=list_words[poz][letter]:
                        #g.write("TEMPLATE 2: ")
                        #g.write(list_words[poz])
                        #g.write('\n')
                        block[poz]=1
                    elif aparitii_lit_cuv_word_tryout[ord(word_tryout[letter])-ord('A')] > (litera_blocata_2[ord(word_tryout[letter])-ord('A')]+litera_blocata_1[ord(word_tryout[letter])-ord('A')]):
                        if aparitii_lit_cuv_lista[ord(word_tryout[letter])-ord('A')] > (litera_blocata_2[ord(word_tryout[letter])-ord('A')]+litera_blocata_1[ord(word_tryout[letter])-ord('A')]):
                            block[poz]=1
                
        if block[poz]==0:
            for letter in range (5):
                if template[letter]==1: #daca am 1 trebuie neaparat sa fie in cuvant
                    if word_tryout[letter]==list_words[poz][letter]:
                        #g.write("TEMPLATE 1 a: ")
                        #g.write(list_words[poz])
                        #g.write('\n')
                        block[poz]=1
                    elif word_tryout[letter] not in list_words[poz]:
                        #g.write("TEMPLATE 1 b: ")
                        #g.write(list_words[poz])
                        #g.write('\n')
                        block[poz]=1
                    elif word_tryout[letter] in list_words[poz] and (aparitii_lit_cuv_word_tryout[ord(word_tryout[letter])-ord('A')] > (litera_blocata_2[ord(word_tryout[letter])-ord('A')]+litera_blocata_1[ord(word_tryout[letter])-ord('A')])):
                        if aparitii_lit_cuv_lista[ord(word_tryout[letter])-ord('A')] > (litera_blocata_2[ord(word_tryout[letter])-ord('A')]+litera_blocata_1[ord(word_tryout[letter])-ord('A')]):
                            #g.write("TEMPLATE 1 c: ")
                            #g.write(list_words[poz])
                            #g.write('\n')
                            block[poz]=1
                    

        if block[poz]==0:
            for letter in range (5):
                if template[letter]==0 and (litera_blocata_1[ord(word_tryout[letter])-ord('A')]==0 and litera_blocata_2[ord(word_tryout[letter])-ord('A')]==0):
                    if word_tryout[letter] in list_words[poz]:
                        #g.write("TEMPLATE 0: ")
                        #g.write(list_words[poz])
                        #g.write('\n')
                        block[poz]=1 
                        break
                    
        poz=poz+1
    
    """
    for i in range (len(list_words)):
        if block[i]==1:
            print(list_words[i])
    """

    for i in range (len(list_words)):
        if block[i]==0:
            remaining_words.append(list_words[i])

    print(len(remaining_words))

    return remaining_words



#main:

f = open('wordlist.txt','r')

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

steps=0

"""

Pt a scadea timpul de rulare o sa fac mai intai pt TAREI feedbacul si lista ce ramane dupa eliminare, 
pentru a nu face iar entropia pe lista initiala de fiecare data

"""
for word in ["ABACA"]:
    
    modified_content_list=content_list[:]

    word_try="TAREI"
    feedback = "00000"
    guess_list = list(word)
    feedback = list(feedback)
        
    for i in range(5):
        if word_try[i] == word[i]:
            feedback[i] = "2"
            guess_list[i] = "0"
        
    for i in range(5):
        if feedback[i] == "0":
            index = None
            try:
                index = guess_list.index(word_try[i])
            except:
                pass
            else:
                guess_list[index] = "0"
                feedback[i] = "1"
        
    feedback="".join(feedback)

    modified_content_list=delete_from_list(word_try, feedback, modified_content_list)
    steps+=1
    print(len(modified_content_list))
    #print(modified_content_list, sep='\n')
"""
    while word_try!=word:
        
        feedback = "00000"
        
        word_try=""
        word_try=word_try+Word_With_Max_Entropy(modified_content_list)
        guess_list = list(word)
        feedback = list(feedback)
        
        for i in range(5):
            if word_try[i] == word[i]:
                feedback[i] = "2"
                guess_list[i] = "0"
        
        for i in range(5):
            if feedback[i] == "0":
                index = None
                try:
                    index = guess_list.index(word_try[i])
                except:
                    pass
                else:
                    guess_list[index] = "0"
                    feedback[i] = "1"
        
        feedback="".join(feedback)

        template=feedback

        modified_content_list=delete_from_list(word_try, template, modified_content_list)
        steps+=1      
"""      
    
print (steps)

#print(Word_With_Max_Entropy(content_list))

"""

ABACA
ABACEE


"""