import math

f = open("wordlist.txt", "r")

content_list = f.readlines()

B3_v2=[]
for i in range(243):
    aux=i
    text =""
    for j in range(5):
        text = text + str(aux % 3)
        aux=aux//3
    B3_v2.append(text)

def entropy(nr_cuvinte_eliminate):
    cuv_totale = len(content_list)
    numarator = cuv_totale - nr_cuvinte_eliminate
    if numarator > 0:
        shanon = (numarator/cuv_totale)*(math.log2((cuv_totale/numarator)))
    else:
        return 0
    return shanon

def entropy_for_word(word):
    sum_entropy = 0
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
    return sum_entropy
#Am verificat ACERB, pana acum cel mai bun cuvant este ABROG, pozitia parcursa: 45
maxim = 0.0
best_word = ""
k = 0
for cuv in content_list:
    entropie = entropy_for_word(cuv)
    cuv = cuv[:5]
    if entropie > maxim:
        maxim = entropie
        best_word = cuv
    print(f"Am verificat {cuv}, pana acum cel mai bun cuvant este {best_word}, pozitia parcursa: {k}")
    k += 1
print(cuv)
print(entropie)
