import urllib
import urllib2
import requests
from bs4 import BeautifulSoup
from urllib import urlretrieve

ext = ['.jpg', '.jpeg', '.png']
def imgDownload(link,x):
	link = link.split('?')[0]
	print '[Getting link ',x,' ] ',link[:],' ... : ',
	for i in ext:
		if i in link:
			try:
				urlretrieve(link, str(x)+i)
				#urllib.urlretrieve(link, str(x)+".jpeg")
				print ' Saved ',str(x)+i
			except:
				print('Failed, connection problem')
			break
		else:
			print 'Finding type of image - ',
			try:
				img = urllib2.urlopen(link)
				q = img.info().type
				q = q.split('/')[1]
			except:
				print 'Error not an image'
			try:
				urlretrieve(link, str(x)+'.'+q)
				print ' Saved ',str(x)+'.'+q
			except:
				print ' Error not valid'
			break

print '[URL] :',
url = raw_input()
r = requests.get(url)
soup = BeautifulSoup(r.content)
l = soup.find_all('img')

x=1
for i in l:
	link = i['src']
	imgDownload(link,x)
	print ' Done'
	x+=1