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
        if currentValue == "playing":
            url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {API_TOKEN}"
            }

            response = requests.get(url, headers=headers)
            data = response.json()

            print("Films currently in theatres:")
            for film in data['results']:
                print(" - " + film['original_title'])
            
except getopt.error as err:
    # output error, and return with an error code
    print (str(err))