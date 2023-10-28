import requests as rq
#from bs4 import BeautifulSoup
from pyquery import PyQuery

# headers_Get = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#         'Accept-Language': 'en-US,en;q=0.5',
#         'Accept-Encoding': 'gzip, deflate',
#         'DNT': '1',
#         'Connection': 'keep-alive',
#         'Upgrade-Insecure-Requests': '1'
#     }

headers_Get = {
    'authority': 'www.google.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,fr;q=0.5,de-CH;q=0.4,es;q=0.3',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Not_A Brand";v="99", "Microsoft Edge";v="109", "Chromium";v="109"',
    'sec-ch-ua-arch': '"x86"',
    'sec-ch-ua-bitness': '"64"',
    'sec-ch-ua-full-version': '"109.0.1518.78"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="99.0.0.0", "Microsoft Edge";v="109.0.1518.78", "Chromium";v="109.0.5414.120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-ch-ua-wow64': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78',
}

# def get_wallpaperscom(q):
#     if hasattr(q,"split"):
#         url="https://wallpapers.com/search/" + "+".join(q.split(" "))
#     elif hasattr(q,"pop") and hasattr(q,"__iter__"):
#         x = ""
#         for x in range(0, len(q)):
#             m = q.pop()

def get_wallpaperscom(*args):
    q="+".join(["+".join(g.split(" ")) for g in args])
    url="https://wallpapers.com/search/" + q
    res = rq.get(url,headers=headers_Get)
    return res.text

def getstuff(f,*args):
    m = f(args)
    return m

def runit(*args):
    f = get_wallpaperscom
    mi = getstuff(f,args)
    return mi

#This has better in t.py
# def google(q):
#     s = requests.Session()
#     q = '+'.join(q.split())
#     url = 'https://www.google.com/search?q=' + q + '&ie=utf-8&oe=utf-8'
#     r = s.get(url, headers=headers_Get)

#     soup = BeautifulSoup(r.text, "html.parser")
#     output = []
#     for searchWrapper in soup.find_all('h3', {'class':'r'}): #this line may change in future based on google's web page structure
#         url = searchWrapper.find('a')["href"] 
#         text = searchWrapper.find('a').text.strip()
#         result = {'text': text, 'url': url}
#         output.append(result)

#     return output
