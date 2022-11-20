import math

from tqdm import tqdm

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
			feedback = ["0" for i in range(5)]

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
				freq_templates[len(templates)-1] = 1

		for i in range(len(templates)):
			entropy_calc += entropy(freq_templates[i], word_list)

		if entropy_calc > max_entropy:
			max_entropy = entropy_calc
			maxEtrpy_word = word

	return maxEtrpy_word


#sterg cuvintele care nu imi convin din lista
def delete_from_list(word_tryout, template, word_list):
    remaining_words = []
    for word in word_list:
        to_add = True
        for index in range(5):
            if template[index] == '2' and word[index] != word_tryout[index]:
                to_add = False
            elif template[index] == '1' and word[index] == word_tryout[index]:
                to_add = False
            elif template[index] == '1' and word_tryout[index] not in word:
                to_add = False
            elif template[index] == '0' and word_tryout[index] in word:
                to_add = False
        if to_add == True:
            remaining_words.append(word)
    return remaining_words

def give_feedback(guess, input):
    feedback = ""
    for i in range (0, 5):
        if input[i] == guess[i]:
            feedback += "2"
        else:
            if input[i] in guess:
                feedback += "1"
            else:
                feedback += "0"


# MAIN Function

def main():
	with open("wordlist.txt","r") as words_file:
		word_list = (words_file.read()).split("\n")
		steps = 0

		'''
		Pt a scadea timpul de rulare o sa fac mai intai pt TAREI feedbackul si lista ce ramane dupa eliminare,
		pentru a nu face iar entropia pe lista initiala de fiecare data
		'''



		for word in tqdm(word_list):
			moded_word_list = word_list[:]

			word_try = "TAREI"
			feedback = ["0" for i in range (5)]

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
				feedback = ["0" for i in range(5)]

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

		print(steps)
		print()
		print(steps / 11454)


# Start Program
main()
