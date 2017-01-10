import mechanize
import urllib
import urllib2
import requests
from urllib import urlretrieve
import sys
from bs4 import BeautifulSoup

br = mechanize.Browser()
#br.set_handle_robots(False) #Important: CAUTION DANGER

def userImg(link,x):
	print 'Downloading Image : '+str(link),
	try:
		urlretrieve(link, str(x)+'.jpg')
		print '  Done'
	except:
		print 'Failed'
def userName(soup):
    k = soup.find_all("span",{"id": "lblName"})
    file = open("name.txt","a+")
    file.write(str(k[0].text)+'\n')
    file.close()
    print '|',;sys.stdout.softspace = False;

def userGender(soup):
    k = soup.find_all("span",{"id": "lblGender"})
    file = open("gender.txt","a+")
    file.write(str(k[0].text)+'\n')
    file.close()
    print '|',;sys.stdout.softspace = False;

def userCollege(soup):
    k = soup.find_all("span",{"id": "lblCollegeName"})
    file = open("college.txt", "a+")
    file.write(str(k[0].text)+'\n')
    file.close()
    print '|',;sys.stdout.softspace = False;

def userRoll(roll):
    k = soup.find_all("span",{"id": "lblCollegeName"})
    file = open("roll.txt", "a+")
    file.write(roll+'\n')
    file.close()
    print '|',;sys.stdout.softspace = False;

def userExam(soup):
    k = soup.find_all("span",{"id": "lblExamName"})
    file = open("exam.txt", "a+")
    file.write(str(k[0].text)+'\n')
    file.close()
    print '|]',

def show(i):
	print 'Name: ',name[i]
	print 'Gender: ',gender[i]
	print 'College: ',college[i]
	print 'Exam :',exam[i]

def userShow(x,y,c):
    file = open('name.txt','r')
    name = file.read().splitlines()
    file.close()
    file = open('gender.txt','r')
    gender = file.read().splitlines()
    file.close()
    file = open('college.txt','r')
    college = file.read().splitlines()
    file.close()
    file = open('exam.txt','r')
    exam = file.read().splitlines()
    file.close()
    file = open('roll.txt','r')
    roll = file.read().splitlines()
    file.close()

    if y == 2:
    	for i in xrange(x-1,len(name)):
    		print 'Name: ',name[i]
    		print 'Rollno', roll[i]
    		print 'Gender: ',gender[i]
    		print 'College: ',college[i]
    		print 'Exam :',exam[i]
    elif y == 1:
    	if c == 'N':
    		print 'Enter name: '
    		na = raw_input()
    		for i in xrange(len(name)):
    			if na in name[i]:
    				print 'Found : '
    				print 'Name: ',name[i]
    				print 'Rollno', roll[i]
    				print 'Gender: ',gender[i]
    				print 'College: ',college[i]
    				print 'Exam :',exam[i]
    				break
    		print 'Not found'
    	elif c == 'R':
    		print 'Enter roll no: '
    		ra = raw_input()
    		for i in xrange(len(roll)):
    			if roll[i] == ra:
    				print 'Found :'
    				print 'Name: ',name[i]
    				print 'Rollno', roll[i]
    				print 'Gender: ',gender[i]
    				print 'College: ',college[i]
    				print 'Exam :',exam[i]
    				break
    		print 'Not found'
    	elif c == 'G':
    		print 'Enter MALE or FEMALE: '
    		ga = raw_input()
    		for i in xrange(len(gender)):
    			if gender[i] == ga:
    				print 'Found :'
    				print 'Name: ',name[i]
    				print 'Rollno', roll[i]
    				print 'Gender: ',gender[i]
    				print 'College: ',college[i]
    				print 'Exam :',exam[i]
    				break
    		print 'Not found'
    	elif c == 'S':
    		print 'Enter number: '
    		sa = int(raw_input())
    		i = sa-1
    		print 'Name: ',name[i]
    		print 'Rollno', roll[i]
    		print 'Gender: ',gender[i]
    		print 'College: ',college[i]
    		print 'Exam :',exam[i]
'''try:
	file = open('roll.txt','r')
	rr = file.read().splitlines()
	file.close()
	rr = rr[-1]
	rr = [-3:]
except:
	rr = 701'''
enroll = #number
count = #number
try:
    file = open('name.txt','r')
    a = file.read().splitlines()
    file.close()
except:
    a = 'a'

print 'Total fetched data: '+str(len(a))
print 'Want to [S]earch or [F]etch data ?'
b = raw_input()

if b == 'F':
	while True:
	    print str(count)+'. Getting EnrollNo. : DX1601'+str(enroll),
	    br.open('http://www.mponline.gov.in/Portal/Services/DAVV/Affiliate/Applications/Exam/AdmitCardHtml.aspx')
	    br.select_form(name='form1')
	    br['txtEnrollNo'] = 'DX1601'+str(enroll)
	    br['ddlSemesterCd'] = ['1SEM']
	    br['drpStatus'] = ['REGULAR']
	    br.submit()
	    soup = BeautifulSoup(br.response().read())
	    if 'Fields are' in str(soup):
	        print '\n**Error occured**'
	        enroll+=1
	        continue
	    else:
	        print '[|',;sys.stdout.softspace = False;
	        roll = 'DX1601'+str(enroll)
	        userName(soup)
	        userGender(soup)
	        userCollege(soup)
	        userRoll(roll)
	        userExam(soup)
	        print '  Done'
	        userShow(count,2,0)
	        im = soup.find_all("img",{"id": "imgPhoto"})
	        im = im[0]['src']
	        link = "http://www.mponline.gov.in/"+str(im)
	        userImg(link,count)
	        print '\n'
	    count+=1
	    enroll+=1
elif b == 'S':
	while True:
		print '[N]ame / [R]ollno / [G]ender / [S]no:'
		c = raw_input()
		userShow(0,1,c)