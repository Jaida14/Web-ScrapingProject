from urllib.request import urlopen, Request
from bs4 import BeautifulSoup




##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.webull.com/quote/us/gainers'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#the tags are all similar, using "div", so we need to differentiate them by class


req = Request(url, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

stock_data = soup.findAll("div", attrs = {"class":"table-cell"})

print(stock_data[:2]) #each row contains 11 elements, and then the next, so count each row by 11; every webpage is different tho

counter = 1

for x in range(5): #we want to iterate 5 times
    name = stock_data[counter].text
    change = round(float(stock_data[counter + 2].text.strip('+').strip("%"))/100, 2) #bc these symbols dont make up a float and divide by 100 instead
    last_price = float(stock_data[counter + 3].text)

    prev_price = round(last_price / (1 + change), 2)

    print(name)
    print(change)
    print(last_price)
    print(prev_price)
    print()

    counter += 11 #bc each row has 11 elemnets






#SOME USEFUL FUNCTIONS IN BEAUTIFULSOUP
#-----------------------------------------------#
# find(tag, attributes, recursive, text, keywords)
# findAll(tag, attributes, recursive, text, limit, keywords)

#Tags: find("h1","h2","h3", etc.)
#Attributes: find("span", {"class":{"green","red"}})
#Text: nameList = Objfind(text="the prince")
#Limit = find with limit of 1
#keyword: allText = Obj.find(id="title",class="text")