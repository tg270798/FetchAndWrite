from urllib.request import urlopen as uReq #urllib to work with urls
from bs4 import BeautifulSoup as soup
import csv


quotes_page = 'https://bluelimelearning.github.io/my-fav-quotes/'
uClient = uReq(quotes_page) #connection open
page_html = uClient.read() 
uClient.close() #closing the connection
page_soup = soup(page_html, "html.parser") #parse and read the data stored in the page_html variable

quotes = page_soup.findAll("p",{"class":"aquote"})
authors = page_soup.findAll("p",{"class":"author"})

finalList = {}
for i,j in zip(quotes,authors):
    q = i.text.strip()
    a = j.text.strip()
    
    finalList[a] = q

print(finalList)


fileName = 'quoteList.csv'
with open(fileName,mode = 'w') as csvfile:
    fieldnames = ['Quote','Author']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for i in finalList:
        writer.writerow({'Quote': finalList[i],'Author':i})

# print(len(quotes),len(authors))
#print(quotes)


# for quote in quotes:
#     quotename = soup.findAll("p", {"class":"aquote"})
#     aquote = quotename[0].text.strip()
    
#     authorname = soup.findAll("p", {"class":"author"})
#     author = authorname[0].text.strip()
    
#     print(aquote,author)