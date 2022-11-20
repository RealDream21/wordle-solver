f = open('wordlist.txt','r')

#crearea listei
file_content=f.read()
content_list=file_content.split("\n")

print (content_list[0])