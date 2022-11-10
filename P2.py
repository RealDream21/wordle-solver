with open('wordlist.txt','r') as f:
	listl=[]
	for line in f:
		strip_lines=line.strip()
		listli=strip_lines.split()
		m=listl.append(listli)
		print(list(line))

g = open('data.out','w')
f.close
g.close

alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
L=[]
x="ABACA"
guess_list="TAIN0"
s="1000A"
s=list(s)
for i in range (0,5):
    if s[i]=="1":
        L.append(x[i])
    if s[i]=="0":
        s[i]=input("litera:")
   # if s[i]==alphabet:





print(L)  
print(s)
print()      
print("".join(s))