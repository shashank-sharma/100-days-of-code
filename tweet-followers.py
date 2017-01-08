import requests
from loklak import Loklak
from bs4 import BeautifulSoup
from collections import *
from collections import Counter
import plotly.plotly as py
from plotly.graph_objs import *

l = Loklak()
def userFollowers(name):
	print '\n[twitter]: 1. Getting user followers . . .',
	try:
		fol = l.user(name)
	except:
		print '[twitter]: Error getting data'
		return 0
	print ' Done'
	return fol['user']['followers_count']

def followersData(name,fol):
	track = 0
	print '\n[twitter]: 2. Getting followers data'
	data = l.user(name,fol,None)
	temp = data['topology']['followers']
	for i in temp:
		file = open("user-database.txt","a+")
		file.write(str(i)+'\n')
		file.close()
		file = open("user-link.txt","a+")
		file.write(i['screen_name']+'\n')
		file.close()
		file = open("user-country.txt","a+")
		try:
			file.write(i['location_country']+'\n')
		except:
			track+=1
		file.close()
	print '[twitter]: 3. Successful'
	print '[twitter]: Total User: '+str(len(temp))
	print '[twitter]: Geolocation collected: '+str(len(temp)-track)
	print '[twitter]: Geolocation not found: '+str(track)

def getUser(user):
	print '[twitter]: Getting user information',
	url = "https://twitter.com/search?q="+user+"&src=typd"
	try:
		r = requests.get(url)
	except:
		print 'Connection Error'
		return 0
	print ' Done'
	soup = BeautifulSoup(r.content)
	h = soup.find_all("div",{"class": "u-textTruncate u-inlineBlock"})
	h = str(h[0].a['href'])
	return h.split('/')[1]


print '[Twitter user]: ',
user = raw_input()
name = getUser(user)
print '[found]: '+str(name)
print 'Lets gather some information\n'

followers = userFollowers(name)
print '[twitter]: Followers ',followers
followersData(name,followers)
file = open('user-country.txt','r')
record = file.read().splitlines()
file.close()

record2 = []
record1 = Counter(record)
print record1
record1 = list(record1)
for i in record1:
	record2.append(record.count(i))

trace0 = Bar(
    x=record1,
    y=record2
)
data = Data([trace0])

py.plot(data, filename = 'basic-line')