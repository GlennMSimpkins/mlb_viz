# script to programmaticaly get the salaries of Major League Baseball 
# players as compiled by JEuston of baseballprospectus.com at 
# http://www.baseballprospectus.com/compensation/cots/
#
# This script was written on Linux, and uses the folowing Python libraries:
# 1) requests
# 2) BeautifulSoup4
# 
# If you do not have these packages, use the folowing comands at your shell:
# $ sudo apt-get install python-pip
# $ sudo pip install requests
# $ sudo pip install BeautifulSoup


# this script is currently a stub.
# print "test"
# needed only for the get function:
import requests

import re

# used to parse the pages html parsing of the needed for web parsing:
from bs4 import BeautifulSoup
r = requests.get('http://www.baseballprospectus.com/compensation/cots/')
#print r
soup = BeautifulSoup(r.text)
print "root soup's on!"

#note to maintainer:
# Periodic manual inspection of 'http://www.baseballprospectus.com/compensation/cots/' 
# should be done to verify the text string for teams
#
full_MLB_team_names = set(['San Francisco Giants', 'Colorado Rockies', 'Los Angeles Dodgers',  'San Diego Padres', 'Arizona Diamondbacks', 'Cincinnati Reds', 'St. Louis Cardinals', 'Pittsburgh Pirates', 'Chicago Cubs', 'Milwaukee Brewers', 'Atlanta Braves', 'Philadelphia Phillies',  'New York Mets', 'Miami Marlins', 'Washington Nationals', 'Oakland Athletics', 'Los Angeles Angels of Anaheim', 'Texas Rangers', 'Houston Astros', 'Seattle Mariners', 'Minnesota Twins', 'Chicago White Sox', 'Detroit Tigers', 'Cleveland Indians', 'Kansas City Royals', 'New York Yankees', 'Boston Red Sox', 'Tampa Bay Rays', 'Baltimore Orioles', 'Toronto Blue Jays'])

dictionary_of_team_links = dict()
links = soup('a')

i = 0
for link in links:
	if link.contents[0] in full_MLB_team_names:
		#print("has link") 
		#set_of_team_links.add(link.get('href'))
		if link.contents[0] not in dictionary_of_team_links:
			dictionary_of_team_links[link.contents[0]] = link.get('href')
			#print link.contents[0]
			#print "Hit, link ", i
			#i +=1
		#if(i==30):
		#	break;
		#else:
		#	print "skip" + link.contents[0]


#need a data structure of requests.get and beautifulsoup objects to replace 
# r2 and soup2 objects gets replaced by an element of an array of requests objects
r2 = requests.get(dictionary_of_team_links['San Francisco Giants'])
soup2 = BeautifulSoup(r2.text)
print("team soup is on!")

#for tag in soup2.find_all(re.compile("google")):
#    print(tag.name)

print soup2.find_all("href", re.compile("google"))


# Idea for sorting the json object
# import json
# 	with open("mlb_salaries.json", "r") as f:
#		d = json.loads(f.read)
#		d['features']=sorted(d[features] lamda x: int(x['properties']['team']['payroll']) )
