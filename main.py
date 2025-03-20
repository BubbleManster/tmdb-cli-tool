import config
import requests
import getopt
import sys

API_TOKEN = config.API_TOKEN

argumentList = sys.argv[1:]

# Long options
long_options = ["type="]

try:
    # Parsing argument
    arguments, values = getopt.getopt(argumentList, "", long_options)
    # checking each argument
    for currentArgument, currentValue in arguments:
        match currentValue:
            case "playing":
                url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
                category = "in cinemas now"
            case "popular":
                url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
                category = "popularity"
            case "top":
                url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
                category = "highest rating"
            case "upcoming":
                url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"
                category = "soon to be released"
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

response = requests.get(url, headers=headers)
data = response.json()

print(f"Ranking films based on {category}:")
for i, film in enumerate(data['results']):
    print(f"{i + 1}. " + film['original_title'])