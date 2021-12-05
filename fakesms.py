#!/usr/bin/env python
import threading
import string
import base64
import urllib.request
import urllib.parse
import os
import time
import sys
import random

try:
    import requests
except ImportError:
    print('ข้อผิดพลาด !! : ไม่ได้ติดตั้งการพึ่งพาบางรายการ')
    print("เกิดข้อผิดพลาดในการนำเข้าไลบรารี 'คำขอ'\ntodo : python3 -m pip install การร้องขอ")
    exit()

# colors
yellow='\033[93m'
gren='\033[92m'
cyan='\033[96m'
pink='\033[95m'
red='\033[91m'
b='\033[1m'
W = '\033[0m'
colors = ['\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;34m', '\033[1;35m', '\033[1;36m']



def clr():
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')

def banner():
    clr()
    logo = """                                                  
\033[96m
    \033[91mMrHacker   \033[95m Hello      \033[96mv1.0   
\033[96m  
                                         """
    print(logo)
    print("\n")
    

def Track() :
  TXTID = input("\033[96m ป้อนรหัสข้อความของ SMS \n\t -->>")
  os.system(f"curl https://textbelt.com/status/{TXTID}")
  input("\nกด Enter เพื่อออก..")
  print("\nขอบคุณที่ใช้ SMS..")
  print("\tเราหวังว่าจะได้พบคุณอีกครั้ง\n พิมพ์ bash Run.sh\n\to Run Again..")
  print("ขอขอบคุณสำหรับเวลาของคุณ...")
  exit()

def update():
    stuff_to_update = ['fakesms.py', 'Run.sh', '.version']
    for fl in stuff_to_update:
        dat = urllib.request.urlopen("https://github.com/1337XQ/Termux-X-SMS/blob/main/" + fl).read()
        file = open(fl, 'wb')
        file.write(dat)
        file.close()
    print('\n\t\tอัพเดทสำเร็จ !!!!')
    print('\tเรียกใช้สคริปต์อีกครั้ง...')
    exit()



clr()
banner()

try:
    urllib.request.urlopen('https://www.google.com')
except Exception:
    print("เกิดข้อผิดพลาดขณะเชื่อมต่ออินเทอร์เน็ต!!!")
    print("\tโปรดเชื่อมต่ออินเทอร์เน็ตเพื่อดำเนินการต่อ...\n")
    input('กำลังออก....\n กด Enter เพื่อออก....')
    exit()
print('\tตรวจสอบการปรับปรุง...')
ver = urllib.request.urlopen("https://raw.githubusercontent.com/1337XQ/Termux-X-SMS/main/.version").read().decode('utf-8')
verl = ''
try:
    verl = open(".version", 'r').read()
except Exception:
    pass
if ver != verl:
    print('\n\t\t มีอัพเดท...')
    print('\tอัปเดต SMS...')
    update()
print("ยินดีด้วย")
print("เวอร์ชันของคุณเป็นเวอร์ชันล่าสุด")
print('\n\tกำลังเริ่ม SMS...\n')
try:
    noti = urllib.request.urlopen("https://raw.githubusercontent.com/1337XQ/Termux-X-SMS/main/.notify").read().decode('utf-8')
    if len(noti) > 10:
        print('\nการแจ้งเตือน : ' + noti + '\n')
except Exception:
    pass


while True:
	print("\033[0mbเครื่องมือนี้ใช้เพื่อส่งข้อความที่ไม่ระบุชื่อ")
	break
type = 0
try:
	if sys.argv[1] == "track":
		type = 1
except Exception:
	type = 0
if type == 1:
	print("ติดตามข้อความที่ไม่ระบุชื่อที่คุณส่งโดยใช้เครื่องมือนี้")
	print()
	Track()
elif type == 0:
	while True:
		print("ป้อนรายละเอียดของบุคคลที่คุณต้องการส่งข้อความที่ไม่ระบุชื่อ")
		cc = input("\033[96m\t ใส่รหัสประเทศ (ไม่มี +): ")
		if '+' in cc:
		        tc = list(cc)
		        tc.remove('+')
		        cc = ''.join(tc)
		        cc = cc.strip()
		if len(cc) >= 4 or len(cc) < 1:
		        print('\n\nรหัสประเทศไม่ถูกต้อง..\n\t\tรหัสประเทศโดยทั่วไปคือ 1-3 หลัก...\n')
		        continue
		pn = input("\033[96mใส่หมายเลขโทรศัพท์(ไม่เติม0) : +" + cc + " ")
		if len(pn) <= 6:
		        print('\n\nหมายเลขโทรศัพท์ไม่ถูกต้อง..\n')
		        continue
		numbe = cc + pn
		if not numbe.isdigit():
		            print('\n\nหมายเลขโทรศัพท์ต้องประกอบด้วยตัวเลขเท่านั้น\n')
		            continue
		receiver = '+' + numbe
		text = input("\033[96m ป้อนข้อความที่จะส่ง : ")
		
		resp = requests.post('https://textbelt.com/text',{
			'phone' : receiver,
			'message' : text ,
			'key' : 'textbelt'
		})
		
		print(resp.json())
		print("ขอขอบคุณสำหรับเวลาของคุณ...")
		break
		if '"success" : true ' in resp.text:
		    print("\033[92m ข้อความที่ส่งประสบความสำเร็จ \033[0m")
		    input('\n\t\tกด Enter เพื่อออก...')
		    banner()
		    exit()
		if '"success" : false ' in resp.text:
		    print("\033[91m เกิดข้อผิดพลาด")
		    print("\033[91m ไม่สามารถส่ง SMS! ")
		    input('\n\t\tกด Enter เพื่อออก...')
		    banner()
		    exit()
		exit() 
