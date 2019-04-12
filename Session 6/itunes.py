from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs"
#open connect
conn = urlopen(url)
#kéo data về dạng thô
raw_data = conn.read()
#decode
text = raw_data.decode("utf8")
# chuyen data ve text
soup = BeautifulSoup(text,"html.parser")

div = soup.find("div",id="main")
#tim tat ca li trong list
li_list = div.find_all("li")

item_list = []
song_list = []
singer_list = []

for li in li_list:
    a = li.h3.a
    b = li.h4.a
    
    title = a.string
    link = url + a["href"]
    artis = b.string
    item ={
        "link":link,
        "title":title,
        "artis":artis
    }
    song_list.append(a)
    singer_list.append(b)
    item_list.append(item)
    print(item_list)
    print("---------------------------")

import pyexcel
pyexcel.save_as(records = item_list,dest_file_name="ituntopsong.xlsx")

from youtube_dl import YoutubeDL

options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
}
dl = YoutubeDL(options)
dl.download(str(song_list)+'-'+str(singer_list))
