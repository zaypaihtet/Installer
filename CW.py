#installer tool by Command Whispers


import sys
import time
import os
RED = "\033[0;31m"
GREEN = "\033[0;32m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
BLUE = "\033[0;34m"
RESTART="\033[0m"
os.system('clear')
print(RED+'ORIGINAL TOOLS OWNER CRD')
print(RED+'This tool is installer tool')
time.sleep(2)
def banner():
	os.system('figlet INSTALLER TOOL'+'|lolcat')
banner()
time.sleep(1)
def by():
	os.system('figlet -f big COMMAND WHISPERS'+'|lolcat')
def clear():
	os.system('clear')
def z():
	print(GREEN+'Thank For Using Our Tool '+RESTART)

def install():
    print(CYAN+'Install Requirements....'+RESTART)
    time.sleep(1)
    os.system('pkg instll python')
    os.system('pkg instll python2')
    os.system('pkg instll python3')
    os.system('pkg instll figlet')
    os.system('pip2 install mechanize')
    os.system('pip2 install requests')
    os.system('pip2 install tqdm')
    os.system('pkg install ruby')
    os.system('gem install lolcat')
    os.system('pip2 install futures')
    os.system('pip2 install requests bs4')

install()
clear()
by()
print(GREEN+"[1] Old acc cracking ")
print(RED+"[2] Web Hacking")
print(CYAN+"[3] Contet Us ")
print(RED+'[4] Exit')
name = int(input(PURPLE+"Enter Number : "+RESTART))
if name == 1:
	print(GREEN+"1.Old acc crack (sensei)")
	print("2.Crack with randon")
	print("3.Random Email crack")
	print("4.Old acc clone (bint)")
	print("5.Auto Crack (IMPERIAL)")
	print("6.Auto clone (indo tool)"+RESTART)
	b=int(input(BLUE+"What You Want to Install: "))
	if b == 1:
		os.system('rm -rf Sensei')
		os.system('git clone https://github.com/BOT-033/Sensei')
		os.system('mv  Sensei ~')
		z()
		os.system("Done....")

	elif b== 2:
		os.system('rm -rf random')
		os.system('git clone https://github.com/lovehacker404/random')
		os.system('mv random ~')
		os.system("Done....")
		z()

	elif b == 3:
		os.system('rm -rf email')
		os.system('git clone https://github.com/lovehacker404/email')
		os.system('mv email ~')
		z()
		os.system("Done....")
	elif b == 4:
		os.system('rm -rf bint')
		os.system('git clone https://github.com/BotolMehedi/bint')
		os.system('mv bint ~')
		os.system('username and pass = botolbana')
		time.sleep(5)
		z()
		os.system("Done....")
		
	elif b == 5:
		os.system('rm -rf IMPERIAL')
		os.system('git clone https://github.com/Hunter-alamin/IMPERIAL')
		os.system('mv IMPERIAL ~')
		z()
		os.system("Done....")
	elif b == 6:
		os.system('rm -rf CRACK-OLD')
		os.system('git clone https://github.com/Dumai-991/CRACK-OLD')
		os.system('mv CRACK-OLD ~')
		z()
		os.system("Done....")

	else:
		print("Wrong number ")
		z()
		os.system('exit')

elif name == 2:
	print(RED+"1.AUTO DEFACE ")
	print('2. SQLMAP')
	print('3.AURO SQL INJECTION & DUMP ADMIN '+RESTART)
	c = int(input(CYAN+"What You Want to install : "))
	if c == 1:
		os.system('rm -rf ZPH-DEFACE')
		os.system('git clone https://github.com/zaypaihtet/ZPH-DEFACE')
		os.system('mv ZPH-DEFACE ~')
		z()
		os.system("Done....")

	elif c== 2:
		os.system('rm -rf sqlmap')
		os.system('git clone https://github.com/sqlmapproject/sqlmap')
		z()
		os.system('mv sqlmap ~')
		os.system("Done....")

	elif c== 3:
		os.system('psqli-pro')
		os.system('git clone https://github.com/Agressiv1njector/psqli-pro')
		os.system('mv  psqli-pro ~')
		z()
		os.system("Done....")

	else:
		print(RED+'Wrong number ')
		z()
		os.system('exit')
		
	
elif name == 3:
	os.system('xdg-open https://www.facebook.com/COMMANDWHISPERS/')
elif name == 4:
	z()
	os.system('exit')
	
