import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today().strftime("%Y-%m-%d")

warren_breakfast = []
warren_lunch = []
warren_dinner = []

west_breakfast = []
west_lunch = []
west_dinner = []

marciano_breakfast = []
marciano_lunch = []
marciano_dinner = []

granby_lunch = []
granby_dinner = []

# Crawler for Warren

URL = "https://www.bu.edu/dining/location/warren/#menu"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

breakfast_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-breakfast"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

lunch_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-lunch"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

dinner_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-dinner"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

for row in breakfast_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    warren_breakfast += [[menu_title, menu_descript]]
  except AttributeError:
    pass

for row in lunch_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    warren_lunch += [[menu_title, menu_descript]]
  except AttributeError:
    pass

for row in dinner_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    warren_dinner += [[menu_title, menu_descript]]
  except AttributeError:
    pass


# Crawler for West

URL = "https://www.bu.edu/dining/location/west/#menu"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

breakfast_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-breakfast"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

lunch_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-lunch"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

dinner_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-dinner"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

for row in breakfast_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    west_breakfast += [[menu_title, menu_descript]]
  except AttributeError:
    pass


for row in lunch_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    west_lunch += [[menu_title, menu_descript]]
  except AttributeError:
    pass


for row in dinner_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    west_dinner += [[menu_title, menu_descript]]
  except AttributeError:
    pass


# Crawler for Marciano

URL = "https://www.bu.edu/dining/location/marciano/#menu"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

breakfast_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-breakfast"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

lunch_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-lunch"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

dinner_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-dinner"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

for row in breakfast_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    marciano_breakfast += [[menu_title, menu_descript]]
  except AttributeError:
    pass

for row in lunch_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    marciano_lunch += [[menu_title, menu_descript]]
  except AttributeError:
    pass

for row in dinner_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    menu_descript = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('p', attrs = {"class":"menu-description"}).text.strip()
    marciano_dinner += [[menu_title, menu_descript]]
  except AttributeError:
    pass


# Granby Crawler

URL = "https://www.bu.edu/dining/location/granby/#menu"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

lunch_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-lunch"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})

dinner_tags = soup.find('div', attrs = {'class':'menu-area-wrapper'}).find('ol', attrs = {"data-menudate":f"{today}"}).find('li', attrs = {"id":f"{today}-dinner"}).find('ol', attrs = {"class":"menu-dishes"}).findAll('li', attrs = {'class':'menu-item menu-main menu-has-warning'})


for row in lunch_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    granby_lunch += [[menu_title]]
  except AttributeError:
    pass

for row in dinner_tags:
  try:
    menu_title = row.find('div', attrs = {"class":"menu-item-wrapper main-with-nutrition"}).find('h4', attrs = {"class":"js-nutrition-open-alias menu-item-title"}).text
    granby_dinner += [[menu_title]]
  except AttributeError:
    pass
