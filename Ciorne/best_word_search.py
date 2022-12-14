import math

f = open("wordlist.txt", "r")

content_list = f.readlines()

B3_v2 = []
for i in range(243):
    aux = i
    text = ""
    for j in range(5):
        text = text + str(aux % 3)
        aux = aux // 3
    B3_v2.append(text)

def entropy(nr_cuv_eliminate):
    nr_cuv_totale = len(content_list)
    nr_cuv_ramase = nr_cuv_totale - nr_cuv_eliminate
    if nr_cuv_ramase > 0:
        shanon = (nr_cuv_ramase/nr_cuv_totale)*(math.log2((nr_cuv_totale/nr_cuv_ramase)))
    else:
        return 0
    return shanon

alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
word_freq = {}
def entropy_for_word(word):
    sum_entropy = 0
    for template in B3_v2:
        nr_cuv_eliminate = 0
        for tryout_word in content_list:
            elim = 0
            for index in range(26):
                word_freq[alphabet[index]] = [0,0]
            for index in range(5):
                if template[index] == "0" and word[index] in tryout_word:
                    elim = 1
                    break
                elif template[index] == "2" and tryout_word[index] != word[index]:
                    elim = 1
                    break
            if elim != 1:
                for index in range(5):
                    if template[index] == "1":
                        word_freq[word[index]][0] += 1
                        if template[index] != "2":
                            word_freq[tryout_word[index]][1] += 1
                for index in range(5):
                    if template[index] == 1 and word_freq[word[index]][0] != word_freq[word[index]][1]:
                        elim = 1
                        break
            nr_cuv_eliminate += elim
        sum_entropy += entropy(nr_cuv_eliminate)
    return sum_entropy
best_word = "AUREI" #se introduce cel mai bun cuvant
maxim = entropy_for_word(best_word) #nu trebuie schimbat nimic, calculeaza pt best_word
k = 743 #ca si k se introcue fix ce este in [], deci nu trb sa calculezi nimic

#Am verificat ACHIT, entropia actuala: 27.648036638297036. Pana acum cel mai bun cuvant este ABTIE,cu entropia 30.05835827752119 pozitia parcursa: [50]
#Am verificat ADAUS, entropia actuala: 25.647092420139366. Pana acum cel mai bun cuvant este ACREI,cu entropia 31.743474933106608 pozitia parcursa: [100]
#Am verificat AVIVA, entropia actuala: 24.24475933323238. Pana acum cel mai bun cuvant este AUREI,cu entropia 35.16518030783676 pozitia parcursa: [743]
#print(f"Am verificat {cuv}, entropia actuala: {entropie}. Pana acum cel mai bun cuvant este {best_word},cu entropia {maxim} pozitia parcursa: [{k}]")

for cuv in content_list[k:]:
    entropie = entropy_for_word(cuv)
    cuv = cuv[:5]
    if entropie > maxim:
        maxim = entropie
        best_word = cuv
    print(f"Am verificat {cuv}, entropia actuala: {entropie}. Pana acum cel mai bun cuvant este {best_word},cu entropia {maxim} pozitia parcursa: [{k}]")
    k += 1

print(cuv)
print(entropie)
