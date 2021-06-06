# Import requests (to download the page)
import requests
# Import BeautifulSoup (to parse what we download)
from bs4 import BeautifulSoup
from datetime import date
import re
import time

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
reading = {}


def loadFile():
    # Dict that will contain keys and values
    with open("reading.txt", "r") as theFile:
        for line in theFile:
            entry = line.strip().split("|")
            print(entry)
            reading[entry[0]] = entry[1]
        return reading


def addDateSuffix(day):
    suffix = ""
    day = 1
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return str(day)+suffix

def setDate():

    day = addDateSuffix(date.today().day)
    year = str(date.today().year)
    month = str(date.today().strftime("%A, %B"))
    today = month + " " + day + " " + year
    print(today)
    return today

# Returns a List of Today's Manga that were released.
def fetchMangaUpdates():
    page = requests.get("https://www.mangaupdates.com/releases.html")
    page.raise_for_status() #if error it will stop the program

    # Gets all the html data
    data = BeautifulSoup(page.text, 'html.parser')
    
    seriesInfoList = data.find('p', "d-inline titlesmall").find_next_sibling().find_all("a",{'title': 'Series Info'})
    todaySeriesTitles = [title.text for title in seriesInfoList]

    #seriesTitles = "".join([str(tag.text + "|") for titles in seriesInfo])
    todaySeriesTitles.append("Solo Leveling")
    print(todaySeriesTitles)

    return todaySeriesTitles

#TODO: Search today's list for if anything I read was updated
def Update(todaySeriesTitles):
    updatedSeries = [title for title in todaySeriesTitles if title in reading]
    print(updatedSeries)
    return

#Multiple Days 
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
    readingInfo = loadFile()
    print(readingInfo)
    #todaySeriesTitles = fetchMangaUpdates()
    #Update(todaySeriesTitles)
    
