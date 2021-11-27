from bs4 import BeautifulSoup
import requests

def get_news():
	resul = {}

	r = requests.get("https://www.air-cosmos.com/actualite/aviation-civile")


	b = BeautifulSoup(r.text,features="html5lib")

	r = b.findAll('div', attrs={"class":"col-md-6"})

	for i in r:

		if i.findAll('span', attrs={"style":"color: inherit;"}) == [] and len(i.findAll('h2', attrs={"class":"title"})) == 1:
			m = i.findAll('h2', attrs={"class":"title"})[0].text +'\n'+ i.findAll('p', attrs={"class":"headline"})[0].text
			img = i.findAll('div')[0]["style"][22:-2]
			resul.append({'title':m,'image':img})
			
