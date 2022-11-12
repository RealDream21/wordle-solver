with open("wordlist.txt","r") as words_file:
    word_list = (words_file.read()).split("\n")

#return ca remaining_words
def delete_from_list(word_tryout, template, word_list):
    remaining_words = []
    for word in word_list:
        to_add = True
        for index in range(5):
            if template[index] == '2' and word[index] != word_tryout[index]:
                to_add = False
            if template[index] == '1' and word[index] == word_tryout[index]:
                to_add = False
            if template[index] == '1' and word_tryout[index] not in word:
                to_add = False
            if template[index] == '0' and word_tryout[index] in word:
                to_add = False
        if to_add == True:
            remaining_words.append(word)
    return remaining_words

print(delete_from_list("TAREI", "20010", word_list))
#daca scot al doilea elif, atunci apare un cuvant ce are pe ac pozitie aceeasi cifra, dar ca template apare la 1
