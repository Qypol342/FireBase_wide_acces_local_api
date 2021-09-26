from pyrebase import pyrebase
from Key import keys
import time

from ActuSpace import actuspace
from ActuAviation import actuaviation
from Actu import actu

api_list =[actuspace, actuaviation,actu]




firebase = pyrebase.initialize_app(key)
db = firebase.database()

while True:
	for i in range(len(api_list)):
		data = api_list[i]()
		db.child("NewsAPI").child(api_list[i].__name__).set(data)

	time.sleep(60*10)





"""
res = db.child("NewsAPI").get()
print(res.val()['actuspace'])
"""