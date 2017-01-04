'''
Movie rating + Summary from imdb
Author: Shashank Sharma
'''
import requests
from bs4 import BeautifulSoup

print 'Enter any movie name'
key = raw_input()                          # Get movie name
key = key.replace(' ','+')                 # To remove spaces and replace with +
print '. . . Getting data . . .'
url = "http://www.imdb.com/find?q=" + key
try:
    r = requests.get(url)
except:
    print 'Connection Error'
soup = BeautifulSoup(r.content)

result_text = soup.find_all("td",{"class": "result_text"})
print '\n\nResult Found:'
count = 1
for item in result_text:
    print str(count)+'. ', item.text
    count+=1

print 'Enter number :'
num = int(raw_input())

movie_url = result_text[num-1].find_all("a")[0]
movie_url = str(movie_url)
movie_url = movie_url.split('"')
movie_url = "http://www.imdb.com" + movie_url[1]

print '\nURL : ' + movie_url
try:
    final = requests.get(movie_url)
except:
    print 'Connection Error'
soup1 = BeautifulSoup(final.content)

rating = soup1.find_all("strong", title = True)
rating = rating[0]['title']
summary = soup1.find_all("div",{"class": "summary_text"})

print '\n\nSUMMARY: ',
for i in summary:
    print i.text,

print '\n\nRating out of 10: ',rating
