with open('wordlist.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		listli=strip_lines.split()
		m=listl.append(listli)
		print(list(line))