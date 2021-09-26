from pyrebase import pyrebase
from Key import keys

from ActuSpace import actuspace
from ActuAviation import actuaviation

api_list =[actuspace, actuaviation]




firebase = pyrebase.initialize_app(key)
db = firebase.database()

for i in range(len(api_list)):
	data = api_list[i]()
	db.child("NewsAPI").child(api_list[i].__name__).set(data)



res = db.child("NewsAPI").get()
print(res.val()['actuspace'])