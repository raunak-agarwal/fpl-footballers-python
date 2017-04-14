import requests
import json


data = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static').json()
# bootstrap-static is a page listing and summarising all the elements of the fpl game
# we retrieve the json object and parse it using .json()
# 'elements' is the branch containing the summary of the player data
# loop inside that and retrieve the extensive player data individually.
# a print statement is at the end 


for i, player in enumerate(data['elements']):
	data['elements'][i]['history'] = requests.get('https://fantasy.premierleague.com/drf/element-summary/' + str(player['id'])).json()
	print ('Retrieving for player id number:', player['id'])
	

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile)
