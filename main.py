# Import requests (to download the page)
import requests
# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup
from datetime import date
import re
import time

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}



def addDateSuffix(day):
    suffix = ""
    day = 1
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return str(day)+suffix

#Wednesday, May 26th 2021


def setDate():

    day = addDateSuffix(date.today().day)
    year = str(date.today().year)
    month = str(date.today().strftime("%A, %B"))
    today = month + " " + day + " " + year
    print(today)
    return today






#List of Urls, Will be a map
urls = {"Solo Leveling":"Where I normally read it"}

def fetchMangaUpdates(mangaName,url):
    page = requests.get(url)
    page.raise_for_status() #if error it will stop the program

    # Gets all the html data
    data = BeautifulSoup(page.text, 'html.parser')
    
    date = data.find('p', "d-inline titlesmall").find_next_sibling().find_all("a",{'title': 'Series Info'})
    theList = "".join([str(tag.text + "|") for tag in date])
    return

def fetch():
    return

def fetchAll():
    return

#Grabs HTML page if new
def addManga(mangaName,url):
    return ""


def listFollowedManga():
    return
    
def remove():
    return

if __name__ == '__main__':
    addManga2("Solo Leveling","https://www.mangaupdates.com/releases.html")
    #addManga("Solo Leveling","https://manganelo.com/manga/pn918005")
    setDate()






#Grabs HTML page if new
def addManga(mangaName,url):
    page = requests.get(url)

    #Check if 200 or 404
    response_code = str(page.status_code)

    # Display the text of the URL in str
    data = page.text

    # Use BeautifulSoup to use the built-in methods
    soup = BeautifulSoup(data,"html.parser")

    # Iterate over all links on the given URL with the response code next to it
    for link in soup.find_all('a'):
        print(f"Url: {link.get('href')} " + f"| Status Code: {response_code}")
