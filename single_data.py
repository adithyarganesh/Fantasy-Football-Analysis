from bs4 import BeautifulSoup as soup
import requests
import cgi
import json

#x = json.opens('player_list.json', 'r') 
val = cgi.FieldStorage()
def index_spider(url):
    
    page = requests.get(url)
    page_html = page.text
    page_soup = soup(page_html , "html.parser")
    #for link in bucket:
    link = page_soup.findAll('span', {'class':'stat'}) 
    #value = link[0].span.text.strip()
    #details = value
    details = {}
    info = page_soup.findAll('div' , {'class':'info'})

    try:
        details["Club"] = info[0].text.strip()
        details["Position"] = info[1].text.strip()
        name = page_soup.findAll('div' , {'class':'name'})[0].text
    except:
        details["Position"] = ""
        details["Club"] = ""
        name = ""
    all_details = page_soup.findAll('div' , {'class':'normalStat'})
    count = 0
    try:
        for ss in link:
            #if ss.text.strip() != "Attack" or ss.text.strip() != "Team Play" or ss.text.strip() != "Discipline" or ss.text.strip() != "Defence":
            #if ss.span.span != NULL:
            idd = ss.text.strip()
            #print(idd)
            try:
                temp = ss.span.text.strip()
            except:
                temp = ""
            #print(temp)
            #print ("id" + id)  
            player_id = idd.replace(temp,"")
            details[player_id.strip()] = temp
            count += 1
        #print (details)

        return details,name
    except ValueError:
        "Do nothing"

    #player_details = json.dumps(details)
    #with open("player_details.json", "w") as f:
    #    f.write(player_details) 
           
    




#index_spider("https://www.premierleague.com/players/2047/Jonathan-Walters/stats")