#Main.py
import requests
import time
from keep_alive import keep_alive
from session import login
from Data import data
import random
import os 



keep_alive()

url = "https://api.thecoinday.app/api/v1/userenergy"

h = {
      "Host": "api.thecoinday.app",
    "content-type": "application/json",
    "cookie": "",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.8.0"
}
l = []
with open("allidtokens.txt","r")as rr:
  l = rr.read().split(",")


l = l[:len(l)-1]


while(True):
  for v,i in enumerate(l):
    print("Account No ",v)
    while(True):
      try:
        data1 = {"data" : ""}
        data1["data"] = data()
        s = login(i)
        h["cookie"]="session\u003d"+s
     
        r = requests.post(url,headers=h,json=data1).json()
        print(r["message"])
      
        if (r["statuscode"] == 400):
          break
      
      except:
        print("Error")
  print("Sleeping For 6 Minutes")
  time.sleep(6*60)
