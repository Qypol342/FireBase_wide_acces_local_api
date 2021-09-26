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
          

def get_image(xml):
  find= 'src="'
  xml = str(xml)
  
  i = xml.index(find)
  end = xml[i+len(find):].index('"')

  return xml[i+len(find):i+len(find)+end]

def sepcial_car_filt(text):
  if '&#8217;' in text:
    i = text.index("&#8217;")
    r ='’'  
    text = text[:i]+r+text[(i+len("&#8217;")):]
    return sepcial_car_filt(text)
  else:
    return text
  

def actuaviation():
    result = requests.get( 
              "https://simpleflying.com/feed/", 
             
    ) 
    rep  =result.text
    #rep2 = json.loads(rep)
    


    tmp = rep
    arti = xml_tools(tmp,"item")
    title = []
    c_s = len("<![CDATA[")
    c_e = len("&#8230;]]>")
    for i in arti:

      title.append({'title':sepcial_car_filt(xml_tools(i,"description")[0][c_s:-c_e]),'img':get_image(xml_tools(i,"content:encoded")[0])})
    return title


