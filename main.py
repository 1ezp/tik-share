import ssl
import threading
from random import randint, choice
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import urlparse
from http import cookiejar

import requests
from pystyle import Colorate, Colors, Write, Add, Center

from Data.UserAgent import UserAgent
from Data.Lists import DeviceTypes, Platforms, Channel, ApiDomain
from utils import *

class BlockCookies(cookiejar.CookiePolicy):
    return_ok = set_ok = domain_return_ok = path_return_ok = lambda self, *args, **kwargs: False
    netscape = True
    rfc2965 = hide_cookie2 = False

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context
done = 0


def Banner():
    clearConsole()
    Banner1 = r"""
╔╦╗  ╦  ╦╔═  ╔═╗  ╦ ╦  ╔═╗  ╦═╗  ╔═╗
 ║   ║  ╠╩╗  ╚═╗  ╠═╣  ╠═╣  ╠╦╝  ║╣ 
 ╩   ╩  ╩ ╩  ╚═╝  ╩ ╩  ╩ ╩  ╩╚═  ╚═╝
        instagram.com/1ezp
"""

    Banner2 = r"""
  ,           ,
 /             \
((__-^^-,-^^-__))
 `-_---' `---_-'
  <__|o` 'o|__>
     \  `  /
      ): :(
      :o_o:
       "-" 
       """

    print(Center.XCenter(Colorate.Vertical(Colors.yellow_to_red, Add.Add(Banner2, Banner1, center=True), 2)))

def sendView():
    global done
    while True:
        proxy         = {f'{proxyType}': f'{proxyType}://{choice(proxyList)}'}
        platform      = choice(Platforms)
        osVersion     = randint(1, 12)
        DeviceType    = choice(DeviceTypes)
        headers       = {
                        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                        "user-agent": choice(UserAgent)
                    }
        appName       = choice(["tiktok_web", "musically_go"])
        Device_ID     = randint(1000000000000000000, 9999999999999999999)
        apiDomain     = choice(ApiDomain)
        channelLol    = choice(Channel)
        URI           = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
        data          = f"item_id={itemID}&play_delta=1"

        try:
            req = requests.post(URI, headers=headers, data=data, proxies=proxy, timeout=5,)
            if '"status_code":0' in req.text:
                done += 1
                print(Colorate.Horizontal(Colors.yellow_to_red, f'Done send: {done}'),end='\r')
        except:
            pass

def sendShare():
    global done
    while True:
        platform = choice(Platforms)
        osVersion = randint(1, 12)
        DeviceType = choice(DeviceTypes)
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": choice(UserAgent)
        }
        appName = choice(["tiktok_web", "musically_go"])
        Device_ID = randint(1000000000000000000, 9999999999999999999)
        apiDomain = choice(ApiDomain)
        channelLol = choice(Channel)
        URI = f"https://{apiDomain}/aweme/v1/aweme/stats/?channel={channelLol}&device_type={DeviceType}&device_id={Device_ID}&os_version={osVersion}&version_code=220400&app_name={appName}&device_platform={platform}&aid=1988"
        data = f"item_id={itemID}&share_delta=1"

        try:
            req = requests.post(URI, headers=headers, data=data)
            if '"status_code":0' in req.text:
                done += 1
                
                print(Colorate.Horizontal(Colors.yellow_to_red, f'Done send: {done}'),end='\r')
        except:
            pass

def clearURL(link):
    parsedURL = urlparse(link)
    host = parsedURL.hostname.lower()
    if "vm.tiktok.com" == host or "vt.tiktok.com" == host:
        UrlParsed = urlparse(r.head(itemID, verify=False, allow_redirects=True, timeout=5).url)
        return UrlParsed.path.split("/")[3]
    else:
        UrlParsed = urlparse(link)
        return UrlParsed.path.split("/")[3]




if (__name__ == "__main__"):
    clearConsole(); Banner()
    VideoURI     = str(Write.Input("Video Link > ", Colors.yellow_to_red, interval=0.0001))
    nThreads     = int(Write.Input("Thread Amount > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    sendType     = int(Write.Input("[0] - Views\n[1] - Shares > ", Colors.yellow_to_red, interval=0.0001)); clearConsole(); Banner()
    itemID       = clearURL(VideoURI)
    proxyChoose  = True
    while proxyChoose:
        proxyType = Write.Input("Select proxy type:\n[0] - http\n[1] - socks4\n[2] - socks5 > ", Colors.yellow_to_red, interval=0.0001)
        if proxyType == "0":
            proxyType = "http"
            proxyChoose = False
        elif proxyType == "1":
            proxyType = "socks4"
            proxyChoose = False
        elif proxyType == "2":
            proxyType = "socks5"
            proxyChoose = False

    proxyList = readProxiesFile()
    clearConsole(); Banner()

    print(Colorate.Horizontal(Colors.yellow_to_red, f"Hits are not counted"))
    print(Colorate.Horizontal(Colors.yellow_to_red, f"Bot started! Check your video stats in 5 minutes !"))

    if sendType == 0:
        sendProcess = sendView
    elif sendType == 1:
        sendProcess = sendShare
    else:
        print(f"Error {sendType}")

    #threading.Thread(target=countThread).start()
    #threading.Thread(target=progressThread).start()
    for i in range(nThreads):
        threading.Thread(target=sendProcess).start()

    #for n in range(nThreads):
    #    threading.Thread(target=proccessThread, args=(sendProcess,)).start()
