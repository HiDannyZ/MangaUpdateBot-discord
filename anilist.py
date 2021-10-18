import requests

#TODO Add in AniList Api to grab in all reading manga listing. 
# Get it in List form and filter it down
# CURRENTLY READING
# PLAN TO READ
# DROPPED
url = 'https://graphql.anilist.co'

query = '''
query { 
    User(search:"hidanny"){
        id
    }
  }
'''

# Currently Reading
currentlyRead = '''
    query($userId: Int) {
        MediaListCollection(userId:$userId, userName:"HiDanny", type:MANGA,status:CURRENT){
            lists{
                entries{
                    media{
                        title{
                            romaji  
                        }
                    }
                }
            }
      }
    }
'''

WatchedAnime = '''{
  Page(page: 1) {
  }
}
'''

query3 = '''{
  Page(page: 1) {
    characters(sort: FAVOURITES_DESC) {
      image {
        large
      }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'id': 15125
}

def allWatched():
    response = requests.post(url, json={'query': WatchedAnime, 'variables': variables})
    page = response.json()




# Make the HTTP Api request
def currentlyReading():
    response = requests.post(url, json={'query': currentlyRead, 'variables': variables})
    page = response.json()
    print(page)
    mediaData = page['data']['MediaListCollection']['lists'][0]['entries']
    print(mediaData)

    allTitles = []
    for media in mediaData:
      title = media['media']['title']['romaji']
      allTitles.append(title)
    return allTitles

if __name__ == '__main__':
  currentlyReading()
  allWatched()