import csv
import wikipedia
from bs4 import BeautifulSoup

footballer_names = []
footballer_data = []

file=open('history.dat','w')

#Open player name CSV file
with open('players.csv', 'rt') as f:
    reader = csv.reader(f)
    counter = 0
    for row in reader:
      if counter > 0:
        footballer_names.append(row[0])
      counter += 1
      

for footballer_name in footballer_names:
  print(footballer_name)
  p = footballer_name
  first_time = True
  html_ver = wikipedia.page(footballer_name, None, True, True, True).html()

  soup = BeautifulSoup(html_ver, 'html.parser')

  array = []
  found = False
  ignore_next = False

#'infobox card' is the class name of the table that Wiki uses for the player information    
  for tr in soup.find("table", {"class":"infobox vcard"}).findChildren('tr'):

    if tr.text.find("Senior career*") > -1:
      found = True
      ignore_next = True
    elif tr.text.find("National team") > -1:
      found = False
      break

    if found == True and ignore_next == False:
      if first_time:
        first_time = False
        continue
      else:
        p += tr.text.split('\n')[0] + ' ' + tr.text.split('\n')[1]
    elif ignore_next == True:
      ignore_next = False

  p = p.replace("\u2013", "-")
  p += '\n'
  file.write("Jugador, %s" % p)

file.close()