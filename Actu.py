import requests
import json




def hashtag(text):
  result = requests.get("http://127.0.0.1:5000/hashtag/" +text) 

  return json.loads(result.text)['hashtaged']



def xml_tools(myhtml,tag):
       res= []
       _tag = "</"+tag+">"
       end_tag = "<"+tag+">"
       for item in myhtml.split(_tag):
              if end_tag in item:
                     res.append(item [ item.find(end_tag)+len(end_tag) : ])
       return res

def xml_image(xhtml):
       find= 'url="'
       j = str(xhtml).index(find)
       end = str(xhtml)[j+len(find):].index('"')
       url = xhtml[j+len(find):j+len(find)+end]
       return(url)

def actu():
    data = []
    url = ('https://www.francetvinfo.fr/titres.rss')
    response = requests.get(url).text
    article = xml_tools(response,'item')
    for i in article:
        data.append({'title':hashtag(xml_tools(i,'title')[0]),'img':xml_image(str(i)),'article':xml_tools(i,'link')[0]})
    return(data)



