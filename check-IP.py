#_author_ = 'yakush'
import os
import json
import urllib.request
gIP = input("[+] Enter IP --> ")
url = "https://ipinfo.io/" + gIP + "/json"
try:
    getInfo = urllib.request.urlopen( url )
except:
    print( "\n[!] - IP not found! - [!]\n" )

infoList = json.load(getInfo)

def whoisIpInfo(ip):
    try:
        myCmd = "whois " + gIP
        whoisInfo = os.popen( myCmd ).read()
        return whoisInfo
    except:
        return "\n [!] -- Error -- [!] \n"

print( "-" * 60)

print( "IP: ", infoList["ip"])
print( "City: ", infoList["city"])
print( "Region: ", infoList["region"])
print( "Country: ", infoList["country"])
print( "Hostname: ", infoList["hostname"])

print( "-" * 60)
print( whoisIpInfo(gIP) )