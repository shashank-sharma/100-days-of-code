import requests
import os
from bs4 import BeautifulSoup

def newChannel(name):
	print '\n\n1. Let\'s create your database'
	file = open(name+'.txt','w')
	file.close()
	file = open(name+'-link.txt','w')
	file.close()
	print '[file]: '+name+'.txt have been created'
	print '[file]: '+name+'-link.txt have been created' 
	if not os.path.isfile('./'+name+'.txt') and not os.path.isfile('./youtube-channel.txt'):
		file = open('favourite.txt','w')
		file.close()
		file = open('youtube-channel.txt','w')
		file.close()
		print '[file]: favourite.txt have been created'
	print 'Done'

def getLink(name,urls):
	file = open('youtube-channel.txt','a')
	file.write(urls+'\n')
	file.close()
	url = urls
	print url
	ch = requests.get(url)

	soup = BeautifulSoup(ch.content)
	l = soup.find_all("a",{"class": "yt-uix-sessionlink yt-uix-tile-link  spf-link  yt-ui-ellipsis yt-ui-ellipsis-2"})
	return l

def updateContent(l,name):
	file = open(name+'.txt','w')
	for i in l:
		temp = i['title']
		try:
			temp = str(temp)
		except:
			temp = 'Error occured'
		file.write(temp+'\n')
	file.close()

def updateLink(l,name):
	file = open(name+'-link.txt','w')
	for i in l:
		temp = i['href']
		temp = str(temp)
		file.write(temp+'\n')
	file.close()

def favouriteList(name):
	print '5. Adding this channel to your favourites',
	file = open('favourite.txt','a')
	file.write(name+'\n')
	file.close()
	print '  Done'


url = "https://www.youtube.com/results?search_query="
print 'Welcome to Youtube-Watch Update'
print '\n\n\nInstructions:'
print 'This program at first create one database and assumes that all the video which are upto date are watched by user. Now whenever you select any channel at starting',
print 'then it will compare your local data with the cloud one. If the local data is equal to cloud one then it means there are no update. If they are not equal then it will show'
print 'those link which are updated and therefore you will be notified about that those particular videos.\n\n\n'
try:
	file = open('favourite.txt','r')
	fav = file.read().splitlines()
	file.close()
	file = open('youtube-channel.txt','r')
	yc = file.read().splitlines()
	file.close()
	print 'Favourite list: '
	x = 1
	for i in fav:
		print str(x),' ',i
		x+=1

	print 'Enter number to get updates regarding that channel else type 0 to add any new channel to your list'
	num = int(raw_input())
except:
	num = 0
if num == 0:
	print '[Channel-name] :',
	name = raw_input()
	print '[youtube]: Getting data ',
	name = name.replace(' ','+')
	user = 1
	r = requests.get(url+name)
	print '.',
	soup = BeautifulSoup(r.content)
	user = soup.find_all('a',{'class': 'yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 g-hovercard yt-uix-sessionlink      spf-link '})
	for i in user:
		temp = i['href']
		temp = temp.split('/')
		if temp[1] == 'user' or temp[1] == 'channel':
			urls = 'http://www.youtube.com'+str(i['href'])
			print '[youtube]: Found ',temp[2]
			print '[youtube]: Let\' prepare your data'
			newChannel(name)
			print '\n\n2. Let\'s get some data related video',
			li = getLink(name,urls)
			print '  Done'
			print '\n\n3. Let me update your content',
			updateContent(li,name)
			print '  Done'
			print '\n\n4. Let me update your links',
			updateLink(li,name)
			print '  Done'
			print '\n\n[youtube]: Channel Successfully updated in your local system'
			favouriteList(name)
		else:
			print '[youtube]: Error not found'
		break
	#if os.path.isfile('./'+name+'.txt'):
	#	newChannel(name)
else:
	name = fav[num-1]
	print '[youtube]: Getting updates for '+name
	el = getLink(name,yc[num-1])
	file = open(name+'-link.txt','r')
	sear = file.read().splitlines()
	file.close()
	file = open(name+'.txt','r')
	sear1 = file.read().splitlines()
	file.close()
	sn = 0
	for i in el:
		if sear[sn] == i['href']:
			print 'No new Update'
			break
		else:
			print '[Update]: http://www.youtube.com/'+i['href']
		sn+=1

	print '\n\n Have look at previous latest videos :\n'
	sn = 1
	for i in xrange(3):
		print str(sn)+' '+sear1[i]+'	 || 	'+'http://www.youtube.com'+sear[i]
		sn+=1
