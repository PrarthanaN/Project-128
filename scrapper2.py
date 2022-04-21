from bs4 import BeautifulSoup as bs
import requests 
import pandas as pd

star = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(star)
soup = bs(page.text, 'html.parser')
star_table = soup.find_all('table')

tempList = []

table_rows = star_table[4].find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    tempList.append(row)

starList = []

starName = []
starDistance = []
starMass = []
starRadius = []

for i in range(1, len(tempList)):
    starName.append(tempList[i][0])
    starDistance.append(tempList[i][5])
    starMass.append(tempList[i][8])
    starRadius.append(tempList[i][9])

data = pd.DataFrame(list(zip(starName, starDistance, starMass, starRadius)), columns = ['starName', 'starDistance', 'starMass', 'starRadius'])

data.to_csv('dwarfStars.csv')