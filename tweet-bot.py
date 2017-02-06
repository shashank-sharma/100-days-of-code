'''
Twitter-bot which lets you to tweet instantly without opening browser.
Time utilized - 1 hrs
Key points - To select form and then tweet it.

'''

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

try:
    import Cookie
    import cookielib
    import mechanize
    import time
    import os
    from getpass import getpass
    from bs4 import BeautifulSoup
    print bcolors.OKGREEN+'Import: OK'+bcolors.ENDC
except:
    print bcolors.FAIL+'Import: FAILED'+bcolors.ENDC
time.sleep(1)



def tweet():
	filename = '/home/vipul/Mythical/100day/A.jpeg'
	print bcolors.WARNING+'Enabling Tweet setting . . .'
	url = 'https://mobile.twitter.com/compose/tweet'
	br.open('https://mobile.twitter.com/compose/tweet')
	br.select_form(nr = 0)
	#br.add_file(open(filename,'r'))
	#br['file'] = filename
	msg = raw_input('Enter your tweet: ')
	br['tweet[text]'] = msg
	print bcolors.WARNING+'Sending...'+bcolors.ENDC
	try:
		br.submit()
		print bcolors.OKGREEN+'Submit: OK'+bcolors.ENDC
	except:
		print bcolors.WARNING+'Submit: Failed'+bcolors.ENDC


print bcolors.OKBLUE+'''
.............................IIII.......
..................ZZ~......?IIIIII?.....
............:.I7=?+Z$$$7ZI7IIIII..,I:...
............,7+?IIII$$$$IIIIIIII,.III7,.
...............+?IIIIIIIIIIIIIIIIIII,...
..................I7IIIIIIIIIIIIIIII....
..................IIIIIIIIIII?+:,=I.....
...............=?IIIIIIIIIII:::::::.....
.,=........,=IIIIIIIIIIIII:::::,:,......
....~?I??IIIIIIIIIIIIIIII:::,:::........
.......+?IIIIIIIIIIIIIII:::::::.. ......
..........~IIIIIIIIIIIII:::::...........
................~?IIIIII=...............
........................................
............. ................. ........
............. ,:::::::::::::::,.........
'''+bcolors.ENDC

if os.path.isfile('./.cookies.txt'):
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    time.sleep(1)
    print bcolors.OKGREEN+'Cookies: FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
    time.sleep(1)
    cookiejar =cookielib.LWPCookieJar()
    br.set_cookiejar(cookiejar)
    cookiejar.load('.cookies.txt', ignore_discard=True, ignore_expires=True)
    br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    print bcolors.OKGREEN+'\nStatus: ACCESS GRANTED'+bcolors.ENDC
    try:
        br.open('https://mobile.twitter.com/')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://mobile.twitter.com/')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    soup = BeautifulSoup(br.response().read())
    #coname = soup.find_all('a',{'class': '_5jlw _3t21'})
    #for i in coname:
    #    print bcolors.OKGREEN+'User: '+str(i.text)+bcolors.ENDC
    #    break


else:
    cookiejar =cookielib.LWPCookieJar('.cookies.txt')
    print bcolors.OKGREEN+'Compiled: Successfully'+bcolors.ENDC
    print bcolors.OKGREEN+'Cookies.txt: NOT FOUND'+bcolors.ENDC
    time.sleep(1)
    try:
        br = mechanize.Browser()
        print bcolors.OKGREEN+'Mechanize Browser: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser Setting: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    try:
        br.set_cookiejar(cookiejar)
        print bcolors.OKGREEN+'Browser cookies: OK'+bcolors.ENDC
    except:
        print bcolors.FAIL+'Browser cookies: FAILED'+bcolors.ENDC
        failno = 1
    time.sleep(1)
    # Robots is not false
    #br.set_handle_robots(False)
    print bcolors.OKGREEN+'Robots settings: OK'+bcolors.ENDC
    failno = 0
    try:
        br.open('https://mobile.twitter.com/login')
        print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
    except:
        cou = 0
        print bcolors.FAIL+'Connection: Not Connected'+bcolors.ENDC
        while True:
            print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
            try:
                br.open('https://mobile.twitter.com/login')
                print bcolors.OKGREEN+'Connection: OK'+bcolors.ENDC
                break
            except:
                cou+=1
            if cou >= 3:
                print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                failno = 1
                break
    if failno == 0:
        br._factory.is_html = True
        try:
            br.select_form(nr = 0)
            print bcolors.OKGREEN+'Form selected: OK'+bcolors.ENDC
        except:
            print bcolors.FAIL+'Form selected: FAILED'+bcolors.ENDC
        print bcolors.BOLD + "Email:" + bcolors.ENDC,
        email = raw_input()
        br['session[username_or_email]'] = email
        passw = getpass()
        print bcolors.OKBLUE+'\nSubmitting:'+ bcolors.ENDC,
        br['session[password]'] = passw
        try:
            br.submit()
            print bcolors.OKGREEN+'OK'+bcolors.ENDC
        except:
            cou = 0
            print bcolors.FAIL+'FAILED'+bcolors.ENDC
            while True:
                print bcolors.WARNING+'Trying again: '+str(cou+1)+'/3'+bcolors.ENDC
                try:
                    br.submit()
                    print bcolors.OKGREEN+'OK'+bcolors.ENDC
                except:
                    cou += 1
                if cou>= 3:
                    print bcolors.FAIL+'Failed Quitting'+bcolors.ENDC
                    failno = 1
                    break

        cookiejar.save()
        soup = BeautifulSoup(br.response().read())

if 'try again' in str(soup):
    print bcolors.FAIL+'Log in: Failed'+bcolors.ENDC
else:
    print bcolors.OKGREEN+bcolors.BOLD+'Log in: Accepted'+bcolors.ENDC
    check = raw_input('Press Enter to continue')
    tweet()

'''
>>> br.select_form(nr = 0)
>>> br['tweet[text]'] = 'Bot testing'
>>> br.submit()

'''