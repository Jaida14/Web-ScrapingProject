'''Find a 'scrappable' cryptocurrencies website where you can scrape the top 5 cryptocurrencies and display as a 
formatted output one currency at a time. The output should display the name of the currency, the symbol (if applicable), 
the current price and % change in the last 24 hrs and corresponding price (based on % change).
Furthermore, for Ethereum, the program should alert you via text if the value gets above $2,000 (so I can sell mine haha)'''


from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from twilio.rest import Client
import keys

client = Client(keys.accountSID, keys.authToken)

TwilioNumber = "+18446250101"

myCellPhone = "+4056261137"


webpage = 'https://crypto.com/price'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

#the tags are all similar, using "div", so we need to differentiate them by class


req = Request(webpage, headers = headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text + "\n")



table_rows = soup.findAll("tr") #each row is tr, but each elemenet in that one row is td 

counter = 0

for row in table_rows[1:6]: #the third row with the states all the way to all the states
    
    td = row.findAll("td")
    percent_data = soup.findAll("div", attrs = {"class":"css-b1ilzc"})
    
    corresponding_price = (float(percent_data[counter].text.replace(",", "").strip("$"))) + ((float(td[4].text.strip("%")) / 100) * float(percent_data[counter].text.replace(",", "").strip("$")))
    #replace is for anything in between and strip is for leading and ending; make sure to close the gap though

    print(f'Name: {td[2].text[1:-3]}')
    print(f'Symbol: {td[2].text[-3:]}')
    print(f'Current Price: {percent_data[counter].text}')
    print(f'% Change (24hrs ago): {td[4].text}')
    print(f'Price (24hrs ago): ${corresponding_price:.2f}')

   
  
    print(" ")

    counter += 1


    if {td[2].text[1:-3]} == "ETH":
        if {float(percent_data[counter].text.replace(",", "").strip("$"))} > 2000.00:
            msg = "Text Message:Price is at {percent_data[counter].text}"
            txtmsg = client.messages.create(to = myCellPhone, from_ = TwilioNumber, body = msg)
            print(txtmsg.status)
            cell = client.cells.create(url = "http://demo.twilio.com/docs/voice.xml", to = myCellPhone, from_ = TwilioNumber)


