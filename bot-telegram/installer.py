import urllib.request
from time import sleep

version = input("Enter the version : ")
link = "http://8888.gigfa.com/bot/bot-v" + version + ".py"
name = "bot-v" + version + ".py"
print(link)
print(name)
print("Downloading ...")
sleep(2)
urllib.request.urlretrieve(link , name)