import math

f = open('wordlist.txt','r')

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

#entropia
def entropy(nr_cazuri_template):
    cuv_totale=len(content_list)

    shanon = (nr_cazuri_template/cuv_totale)*(math.log2((cuv_totale/nr_cazuri_template)))
    return shanon


freq_template=[0 for i in range(243)]

templates=[]

pos_temp=0

entropy_max=0.0
word_entropy_max=[""]

g = open('data.out.txt','w')

for word in content_list: # pt cuvantul asta eu primesc feedback
    
    pos_temp=0
    entropy_calc=0.0

    templates=[]

    for i in range(243):
        freq_template[i]=0
    for word_tryout in content_list: #asta e guess
        

        myInput = word
        guess=word_tryout
        feedback = "00000"
        guess_list = list(guess) # lista din literele cuv
        feedback = list(feedback)

        for i in range(5):
            if myInput[i] == guess[i]:
                feedback[i] = "2"
                guess_list[i] = "0"

        for i in range(5):
            if feedback[i] == "0":
                index = None
                try:
                    index = guess_list.index(myInput[i])
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
        entropy_calc+=entropy(freq_template[i])

    if entropy_calc>entropy_max:
        entropy_max=entropy_calc
        word_entropy_max[0]=word

g.close()

print()
print(str(word_entropy_max[0]), entropy_max, sep=" ")

