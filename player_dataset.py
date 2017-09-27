import json
from bs4 import BeautifulSoup as soup
import requests
import cgi
from single_data import index_spider
val = cgi.FieldStorage()

#def data_set():
with open('player_list.json') as json_data:
	d = json.load(json_data)
	json_data.close()

#print(d)
dataset = {}
details = {}
count = 0
while count < len(d):
	#print (d[str(count)])
	link = "https:"+d[str(count)].replace("overview","stats")
	print (link)
	details, name = index_spider(link)
	dataset[name] = details
	count +=1

complete_data = json.dumps(dataset)
with open("fpl_data.json", "w") as f:
	f.write(complete_data)

	#return dataset
