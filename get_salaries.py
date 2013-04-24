# script to programmaticaly get the salaries of Major League Baseball 
# players as compiled by JEuston of baseballprospectus.com at 
# http://www.baseballprospectus.com/compensation/cots/

# This script may require the Beautiful Soup library

# this script is currently a stub.

print "test"

# needed only for the get function:
import requests as rq

import re

# this may be needed for html parsing of the needed for web parsing:
from bs4 import BeautifulSoup
r = rq.get('http://www.baseballprospectus.com/compensation/cots/')
print r
