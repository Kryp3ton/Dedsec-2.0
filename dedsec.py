#!/usr/bin/env python2.7
#
#  
#  

#  ______  _____ ______  _____  _____  _____ 
#  |  _  \|  ___||  _  \/  ___||  ___|/  __ \
#  | | | || |__  | | | |\ `--. | |__  | /  \/
#  | | | ||  __| | | | | `--. \|  __| | |    
#  | |/ / | |___ | |/ / /\__/ /| |___ | \__/\
#  |___/  \____/ |___/  \____/ \____/  \____/
#                                        
#                                       ~@~ coded by Kryp3ton ~@~

import sys
import argparse
import os
import time
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
#import requests
import base64
from getpass import getpass
from commands import *
from sys import argv
from platform import system
from urlparse import urlparse
from xml.dom import minidom
from optparse import OptionParser
from time import sleep
##########################
os.system('clear')
os.system('clear')
os.system('clear')
os.system('clear')
os.system('clear')

directories = ['/uploads/', '/upload/', '/files/', '/resume/', '/resumes/', '/documents/', '/docs/', '/pictures/', '/file/', '/Upload/', '/Uploads/', '/Resume/', '/Resume/', '/UsersFiles/', '/Usersiles/', '/usersFiles/', '/Users_Files/', '/UploadedFiles/',
               '/Uploaded_Files/', '/uploadedfiles/', '/uploadedFiles/', '/hpage/', '/admin/upload/', '/admin/uploads/', '/admin/resume/', '/admin/resumes/', '/admin/pictures/', '/pics/', '/photos/', '/Alumni_Photos/', '/alumni_photos/', '/AlumniPhotos/', '/users/']
shells = ['wso.php', 'shell.php', 'an.php', 'hacker.php', 'lol.php', 'up.php', 'cp.php', 'upload.php',
          'sh.php', 'pk.php', 'mad.php', 'x00x.php', 'worm.php', '1337worm.php', 'config.php', 'x.php', 'haha.php']
upload = []
yes = set(['yes', 'y', 'ye', 'Y'])
no = set(['no', 'n'])




dedeseclogo = """\033[0m
  _____    ______   _____     _____   ______    _____ 
 |  __ \  |  ____| |  __ \   / ____| |  ____|  / ____|
 | |  | | | |__    | |  | | | (___   | |__    | |     
 | |  | | |  __|   | |  | |  \___ \  |  __|   | |     
 | |__| | | |____  | |__| |  ____) | | |____  | |____ 
 |_____/  |______| |_____/  |_____/  |______|  \_____|                                        
 \033[91m"""
def menu():
    print (dedseclogo + """\033[1m
   [!] Coded By Kryp3ton [!]
\033[0m
   {1}--ARP Poisoner
   {2}--Clipboard Logger
   {3}--Fuzzer
   {4}--Key Logger
   {5}--Mac Changer
   {6}--Network Scanner
   {7}--Password Genrator
   {0}--Update DEDSEC
   {98}-Descrizione dei tool
   {99}-Exit
 """)
    choice = raw_input("DEDSEC~# ")
    os.system('clear')
    if choice == "1":
        ARP()
    elif choice == "2":
        clipboard()
    elif choice == "3":
        fuzzer()
    elif choice == "4":
        keylogg()
    elif choice == "5":
        mac()
    elif choice == "6":
        netwscan()
    elif choice == "7":
        psswgen()
    elif choice == "0":
        updatededsec()
     elif choice == "0.1":
        descr()
    elif choice == "99":
        clearScr(), sys.exit()
    elif choice == "":
        menu()
    else:
        menu()


def updatededsec():
    print ("Questo tool puo essere utilizzato solo su sitemi linux o simili. ")
    choiceupdate = raw_input("Continuare Y / N: ")
    if choiceupdate in yes:
        os.system("git clone https://github.com/Kryp3ton/Dedsec-2.0.git")
        os.system("cd  && sudo bash ./update.sh")
        os.system("DEDSEC")

def ARP():
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/ARP-Poisoner/")
    os.system("python3 arpPoison.py")

def clipboard()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Clipboard-Logger")
    os.system("python3 clipboardLogger.py")

def fuzzer()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Fuzzer/")
    os.system("python3 fuzzer.py")

def keylogg()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Key-Logger/")
    os.system("python3 my_key_logger.py")

def mac()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Mac-Changer/")
    os.system("python3 mac-changer.py")

def netwscan()
    os.system("clear")
    os.system("cd cd /usr/share/doc/DEDSEC_toolbox/tool/Network-Scanner/")
    os.system("python3 network-scanner.py")

def psswgen()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Secure-Password-Generator/")
    os.system("python3 password-gen.py")

def descr()
    os.system("clear")
    os.system("cd /usr/share/doc/DEDSEC_toolbox/tool/Descrizione/")
    os.system("cat descrizione.txt")

