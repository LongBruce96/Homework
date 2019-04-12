from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.apple.com/itunes/charts/songs"

conn = urlopen(url)
raw_data = conn.read()
text = raw_data.decode("utf8")
soup = BeautifulSoup(text,"html.parser")

div = soup.find("div",id="main")
li_list = div.find_all("li")

item_list = []

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

    item_list.append(item)
    print(item_list)
    print("---------------------------")

import pyexcel
pyexcel.save_as(records = item_list,dest_file_name="ituntopsong.xlsx")
