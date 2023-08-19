# Will Grab the OP of anime on your list
import requests

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def getAniListExternalId():
    return

def getAnimeId(externalId):
    url = 'https://staging.animethemes.moe/api/resource?filter[external_id]=+'+str(externalId)+'&filter[site]=AniList&include=anime'
    response = requests.get(url, headers=header)   
    page = response.json()
    return page

def getVideo(url):
    response = requests.get(url, headers=header)   
    page = response.json()
    synopsis = page['anime'][0]['synopsis']
    videoUrlLink = page['anime'][0]['themes'][0]['entries'][0]['videos'][0]['basename']
    return videoUrlLink



if __name__ == '__main__':
    url = 'https://staging.animethemes.moe/api/anime?filter[anime][id]=1557&include=themes.entries.videos,themes.song.artists'
    #url ="https://staging.animethemes.moe/api/anime/bakemonogatari"

    print(getAnimeId(120120))
    #print(getVideo(url))
    