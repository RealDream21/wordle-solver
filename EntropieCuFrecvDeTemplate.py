import math

f = open('wordlist.txt','r')

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

freq_template=[0 for i in range(243)]

templates=[]

templates.append("20000")

print (templates)

print()

pos_temp=0

try:
    pos_temp=templates.index("20002")
except:
    templates.append("20002")

print()

print (templates)

#for word in content_list:
    #for word_tryout in content_list:
