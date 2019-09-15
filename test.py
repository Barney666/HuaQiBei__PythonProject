import os
import wget
url='http://quotes.money.163.com/service/zysjb_300762.html?type=report'
path="300762.csv"

try:
    wget.download(url=url,out=path)
except:print("FUCK")

