import math

from tqdm import tqdm

def entropy(template_freq, word_list):

	template_ratio = template_freq / len(word_list)
	shanon=template_ratio * math.log2(len(word_list)/template_freq)

	return (shanon)

def max_entropy_word(word_list):
	
	if len(word_list) == 1:
		return word_list[0]

	max_entropy = 0.0

	maxEtrpy_word = ""

	for word in tqdm(word_list): # pt cuvantul asta eu primesc feedback
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

		"""
		g=open("solutii.txt","w")

		g.write(word)
		g.write('\n')

		for i in range(len(templates)):
			g.write (templates[i])
			g.write (" ")
			g.write (str(freq_templates[i]))
			g.write ('\n')
		
		g.write('\n')
		g.write('\n')

		g.close()

		"""

		for i in range(len(templates)):
			entropy_calc += entropy(freq_templates[i], word_list)

		if entropy_calc > max_entropy:
			max_entropy = entropy_calc
			maxEtrpy_word = word
		
    
	print (max_entropy)

	return maxEtrpy_word
	

with open("wordlist.txt","r") as words_file:
	
	word_list = (words_file.read()).split("\n")
    
	print (max_entropy_word(word_list))