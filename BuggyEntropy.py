import math

# GET ASCII CODE OF LETTER | - "A"
def ordA(letter):
	return ord(letter) - ord("A")


#entropia
def entropy(template_freq, word_list):
	template_ratio = template_freq / len(word_list)
	return (template_ratio * -math.log2(template_ratio))


#returneaza cuvantul cu cea mai mare entropie
def max_entropy_word(word_list):
	if len(word_list) == 1:
		return word_list[0]

	max_entropy = 0.0
	maxEtrpy_word = ""

	for word in word_list: # pt cuvantul asta eu primesc feedback
		freq_templates = [0 for i in range(243)]
		templates = []

		entropy_calc = 0.0
        
		for word_to_guess in word_list: #asta e guess
			word_try = word
			feedback = [0 for i in range(5)]
			
			for i in range(5):
				if word_try[i] == word_to_guess[i]:
					feedback[i] = "2"

			for i in range(5):
				if feedback[i] == "0":
					if word_to_guess.find(word_try[i]) > -1:
						feedback[i] = "1"
            
			feedback = "".join(feedback)

			try:
				freq_templates[templates.index(feedback)] += 1
			except:
				templates.append(feedback)
				freq_templates[-1] = 1

		for i in range(len(templates)):
			entropy_calc += entropy(freq_templates[i], word_list)

		if entropy_calc > max_entropy:
			max_entropy = entropy_calc
			maxEtrpy_word = word

	return maxEtrpy_word


#sterg cuvintele care nu imi convin din lista
def delete_from_list(word_tryout, template, word_list):
	remaining_words = []
	block = [0 for i in range(len(word_list))]

	listBloc_1 = [0 for i in range(26)] #practic aici pun de cate ori imi apare litera in cuvant
                                        #in functie de cati de 1 am
    
	listBloc_2 = [0 for i in range(26)] #practic aici pun de cate ori imi apare litera in cuvant
                                        #in functie de cati de 2 am

	word_tryout_letter_ap=[0 for i in range(26)]

	for letter in word_tryout:
		i = 0
		word_tryout_letter_ap[ordA(letter)] += 1
		if template[i] == "1":
			listBloc_1[ordA(letter)] += 1 #daca litera imi apare in cuvant cu temp 1 cresc aparitiile
		elif template[i] == "2":
			listBloc_2[ordA(letter)] += 1 #daca litera imi apare in cuvant cu temp 2 cresc aparatiile
		i += 1

	index = 0
	while index < len(word_list):
		letter_ap = [0 for i in range(26)] #aparitiile literei cuvantului din lista
        
		for letter in word_list[index]:
			letter_ap[ordA(letter)] += 1

		for letter1 in word_tryout:
			if listBloc_1[ordA(letter1)] > 0 or listBloc_2[ordA(letter1)] > 0: #daca litera mea exista in cuvant, adica am cel putin o val de 1 sau de 2 atunci ma uit in cuvantul meu
				for letter2 in word_list[index]:
					if letter1 == letter2: #daca litera mea e in cuv atunci verific daca imi apare de mai multe ori sau nu
						if listBloc_1[ordA(letter1)] + listBloc_2[ordA(letter1)] > letter_ap[ordA(letter2)]:
							block[index] = 1 # daca litera mea apare de mai multe ori decat in cuvantul incercat, atunci elimin cuvantul din lista ca nu e posibil sa primesc tipul ala de feedback pe el
            
		if block[index] == 0:
			for letter in word_tryout:
				i = 0
				if template[i] == "2":
					if letter != word_list[index][i]:
						block[index] = 1
					elif word_tryout_letter_ap[ordA(letter)] > (listBloc_2[ordA(letter)] + listBloc_1[ordA(letter)]):
						if letter_ap[ordA(letter)] > (listBloc_2[ordA(letter)] + listBloc_1[ordA(letter)]):
							block[index] = 1
				i += 1
        
		if block[index] == 0:
			for letter in word_tryout:
				i = 0
				if template[i] == "1": #daca am 1 trebuie neaparat sa fie in cuvant
					if letter == word_list[index][i]:
						block[index] = 1
					elif letter not in word_list[index]:
						block[index] = 1
					elif word_tryout_letter_ap[ordA(letter)] > listBloc_2[ordA(letter)] + listBloc_1[ordA(letter)]:
						if letter_ap[ordA(letter)] > listBloc_2[ordA(letter)] + listBloc_1[ordA(letter)]:
							block[index] = 1
				i += 1
        
		if block[index] == 0:
			for letter in word_tryout:
				i = 0
				if template[i] == "0" and listBloc_1[ordA(letter)] == 0 and listBloc_2[ordA(letter)] == 0:
					if letter in word_list[index]:
						block[index] = 1
						break
				i += 1
		index += 1

	for i in range (len(word_list)):
		if block[i] == 0:
			remaining_words.append(word_list[i])

	return remaining_words


# MAIN Function
def main():
	with open("wordlist.txt","r") as words_file:
		word_list = (words_file.read()).split("\n")
		steps = 0

		'''
		Pt a scadea timpul de rulare o sa fac mai intai pt TAREI feedbackul si lista ce ramane dupa eliminare,
		pentru a nu face iar entropia pe lista initiala de fiecare data
		'''

		for word in word_list:
			moded_word_list = word_list[:]

			word_try = "TAREI"
			feedback = [0 for i in range(5)]
                
			for i in range(5):
				if word_try[i] == word[i]:
					feedback[i] = "2"
                
			for i in range(5):
				if feedback[i] == "0":
					if word.find(word_try[i]) > -1:
						feedback[i] = "1"
                
			feedback = "".join(feedback)
			moded_word_list = delete_from_list(word_try, feedback, moded_word_list)
			steps += 1

			while word_try != word:
				word_try = max_entropy_word(moded_word_list)
				template = [0 for i in range(5)]

				for i in range(5):
					if word_try[i] == word[i]:
						feedback[i] = "2"
                
				for i in range(5):
					if feedback[i] == "0":
						if word.find(word_try[i]) > -1:
							feedback[i] = "1"
                
				template = "".join(template)

				moded_word_list = delete_from_list(word_try, template, moded_word_list)
				steps += 1
        
		print(steps)
		print()
		print(steps / 11454)


# Start Program
main()
