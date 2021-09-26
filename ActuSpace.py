import requests 
import json




def hashtag(text):
  result = requests.get("http://127.0.0.1:5000/hashtag/" +text) 

  return json.loads(result.text)['hashtaged']


def actuspace():
    result = requests.get( 
              "https://api.spaceflightnewsapi.net/v3/articles", 
             
    ) 
    rep  =result.text
    rep2 = json.loads(rep)
    clean = []
    for i in rep2:
      if len(i['summary']) < 260:

        clean.append({'title':hashtag(i['summary']), 'img':i['imageUrl']})
      elif len(i['title']) < 260:
        clean.append({'title':hashtag(i['summary']), 'img':i['imageUrl']})

    return clean


