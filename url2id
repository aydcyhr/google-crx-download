import re
with open('url.txt', 'r') as x:
	for line in x:
		url = line.replace('\n', '')
		tmp = re.compile('\w*id=\w*')
		id = tmp.search(url)
		print(id.group())
		message = id.group()
		fp=open("id.txt","a+",encoding="utf-8")
		fp.write(message+'\n')
		fp.close()
