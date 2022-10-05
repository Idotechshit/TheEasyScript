# Imports
import pyfiglet
from os import chdir as cd
import os
import time
import webbrowser

# Spoofing
def spoofing():
	os.system('clear')

	banner = open('banner.txt', 'r', encoding='utf-8')
	print(banner.read)

	banner2 = pyfiglet.figlet_format('SPOOFING')
	print(banner2)

	print('1. RANDOM MAC')
	print('2. SPOOF RECV EMAIL')
	print('99. MAIN MENU')

	nbc = input('TES~')

	if nbc == '1':
		os.system('ifconfig')

		interface = input('Interface:')

		os.system(f"sudo ifconfig {interface} down")

		os.system(f"sudo macchanger -r {interface}")

		os.system(f"sudo ifconfig {interface} up")

	if nbc == '2':
		webbrowser.open('https://temp-mail.org/en/')

	if nbc == '99':
		mainmenu()

# System Tools
def systemtools():
	os.system('clear')

	banner = open('banner.txt', 'r', encoding='utf-8')
	print(banner.read)

	banner2 = pyfiglet.figlet_format('SYS TOOLS')
	print(banner2)

	print('1. ENABLE MON MODE')
	print('2. DISABLE MON MODE')
	print('99. MAIN MENU')

	nbc = input('TES~')

	if nbc == '1':

		os.system('ifconfig')

		interface = input('Interface:')

		os.system('sudo airmon-ng check kill')

		os.system(f"sudo airmon-ng start {interface}")

	if nbc == '2':

		os.system('ifconfig')

		interface = input('Interface:')

		os.system(f"sudo airmon-ng stop {interface}")

		os.system('sudo service NetworkManager start')

	if nbc == '99':
		mainmenu()


# Info Gather
def info():
	os.system('clear')

	banner = open('banner.txt', 'r', encoding='utf-8')
	print(banner.read)

	banner2 = pyfiglet.figlet_format('WIRELESS ATTACKS')
	print(banner2)

	print('1. NMAP')
	print('2. NIKTO')
	print('99. MAIN MENU')

	nbc = input('TES~')

	if nbc == '1':
		target = input('Target:')

		os.system(f"sudo nmap -Pn -A {target}")


	if nbc == '2':
		host = input('Host:')

		os.system(f"sudo nikto -h {host}")

	if nbc == '99':
		mainmenu()


# BruteForce
def bruteforce():
	os.system('clear')

	banner = open('banner.txt', 'r', encoding='utf-8')
	print(banner.read())

	banner2 = pyfiglet.figlet_format('BRUTEFORCE')
	print(banner2)


	print('1. FACEBOOK')
	print('2. INSTAGRAM')
	print('99. MAIN MENU')

	nbc = input('TES~')

	if nbc == '1':
		email = input('Users Email:')
		wordlist = input('wordlist:')

		cd('Scripts')
		cd('Facebom')
		os.system(f"sudo python3 faceboom.py -t {email} -w {wordlist}")

	if nbc == '2':
		username = input('Username:')
		wordlist = input('Wordlist:')
		proxy = input('Proxy List')

		cd('Scripts')
		cd('Instagram-')

		os.system(f"python3 instagram.py -u {str(username)} -p {str(wordlist)} -px {str(proxy)}")



	if nbc == '99':
		mainmenu()

# Main Menu
def mainmenu():
	os.system('clear')

	banner = open('banner.txt', 'r', encoding='utf-8')
	print(banner.read())

	print('1. BRUTEFORCE')
	print('2. INFORMATION GATHER')
	print('3. SYSTEM TOOLS')
	print('4. SPOOFING')

	nbc = input('TES~')

	if nbc == '1':
		bruteforce()


	if nbc == '2':
		info()

	if nbc == '3':
		systemtools()


	if nbc == '4':
		spoofing()

mainmenu()
