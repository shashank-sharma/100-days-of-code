'''
Author: Shashank Sharma

Enter any playlist link and then it will scrape all the link and save it in
youtube-links.txt file. After saving it will ask to type those numbers which
you don't want to download and then those serial number videos will be skipped.

'''
from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import youtube_dl

def ytDownload(link):
    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    return 1
print '[URL] :',
url = raw_input()
print('[Getting data]:'),
# If URL is taken while watching from playlist then it will get real link.

url = url.split('&')
url = "https://www.youtube.com/playlist?"+url[1]
try:
    r = requests.get(url)
except:
    print(' [Connection Error]')
soup = BeautifulSoup(r.content)
print('Done')

links = soup.find_all("a",{"class": "pl-video-title-link yt-uix-tile-link yt-uix-sessionlink  spf-link "})
count = 0
completed = 0
file = open("youtube-links.txt","w")
for i in links:
    url = str(i['href'])
    url = url.split('&')
    file.write("https://www.youtube.com%s\n" % url[0])
    count+=1

file.close()
print('[download]: '+str(count)+' links found')


print('[download]: All links are saved in youtube-links.txt')
print("[download]: Enter those numbers which you don't want to download like: 1 2 3")
ignore = map(int, raw_input().split())

x = 1
file = open("youtube-links.txt","r")
for i in file:
    if x in ignore:
        print ('[download '+ str(x)+'/'+str(count)+'] : Skip')
    else:
        print ('[download '+ str(x)+'/'+str(count)+']')
        completed += ytDownload(i)
    x+=1
file.close()

print('\n\n\n[download]: Completed '+str(completed)+'/'+str(count-len(ignore)))
