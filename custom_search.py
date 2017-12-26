from bs4 import BeautifulSoup as soup
import requests
import cgi
val = cgi.FieldStorage()
def index_spider(size):
	pg = 1
	count = 1
	topic = input("Enter the topic u wish to fetch details on: ")
	#topic = val.getvalue('text')
	topic = topic.replace(' ','+')
	while count <= size :
		url = "https://www.bing.com/search?q=" + topic + "&first=" + str(pg) + "&FORM=PERE1"
		pg = pg + 10
		count += 1
		page = requests.get(url)
		page_html = page.text
		page_soup = soup(page_html , "html.parser")
		for link in page_soup.findAll('li' , {'class':'b_algo'}) :
			href = link.a['href']
			print(href)
			page_spider(href)

def page_spider(url):

	page = requests.get(url)
	page_html = page.text
	page_soup = soup(page_html , 'html.parser')
	for link in page_soup.findAll('a') :
		if link.get('href') is not None:
			href = link.get('href')
			if href.find('/') == 0 :
				href = "\t\tlinks in page: " + url +  href
				href = href.replace('//','/')
				href = href.replace('https:/', 'http:/')
				href = href.replace('http:/', 'http://')
				print(href)

			else :
				href = "\t\tlinks in page: " + href
				href = href.replace('//','/')
				href = href.replace('https:/', 'http:/')
				href = href.replace('http:/', 'http://')
				print(href)


pages = input("number of pages:  ")
index_spider(int(pages))

