import requests

#TODO Add in AniList Api to grab in all reading manga listing. 
# Get it in List form and filter it down
# CURRENTLY READING
# PLAN TO READ
# DROPPED


# Populate Reading List with Everything I am reading

# Here we define our query as a multi-line string
query = '''
# Define which variables will be used in the query (id)
query { 
    User(search:"hidanny"){
        id
    }
  }
'''
query2 = '''
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

# Make the HTTP Api request
def currentReading():
    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query2, 'variables': variables})
    page = response.json()
    mediaData = page['data']['MediaListCollection']['lists'][0]['entries']
    print(mediaData)

    for media in mediaData:
      title = media['media']['title']['romaji']
      print(title)
    