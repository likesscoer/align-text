from bs4 import BeautifulSoup
import requests, random


# Donwload website
link = "https://likesscoer.github.io"
r = requests.get(link, allow_redirects= True)

open('likesscocer.txt', 'wb').write(r.content)



# Remove HTML tags
f = open('likesscocer.txt', "r")
remove_html = BeautifulSoup(f, "lxml").text


new_text = open("newtex.txt", "w")
new_text.write(remove_html)
new_text.close()




# align 40
f = open('newtex.txt', 'r')
for i in range(83):
	x = f.readline()
	line = x[:40] + '\n'
	nt = open('align40.txt', 'a')
	nt.write(line)
	nt.close()


# align 60
f = open('newtex.txt', 'r')
for i in range(83):
	x = f.readline()
	line = x[:60] + '\n'
	nt = open('align60.txt', 'a')
	nt.write(line)
	nt.close()




# Randomly shuffle the paragraphs
f = open('newtex.txt', 'r')
lines = []
for i in range(83):
	x = f.readline()
	lines.append(x)

random.shuffle(lines)

for i in lines:
	line = i[:60] + '\n'
	sh = open('randomshuffle.txt', 'a')
	sh.write(line)
	sh.close()