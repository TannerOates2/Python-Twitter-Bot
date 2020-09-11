from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.cnbc.com/quotes/?symbol=.DJI"

# We use try-except in case the request was unsuccessful because of
# wrong URL
try:
   page = urlopen(url)
except:
   print("Error opening the URL")


soup = BeautifulSoup(page, 'html.parser')

content = soup.find('div', {"class": "table-container"})



table = ''
for i in content.findAll('span'):
    table = table + ' ' +  i.text
print(table)

# Saving the scraped text
with open('scraped_text.txt', 'w') as file:
    file.write(table)
