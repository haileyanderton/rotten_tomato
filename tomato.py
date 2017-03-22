from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://www.rottentomatoes.com")
bsObj = BeautifulSoup(html, "html.parser")
f = open("tomato.txt", 'a')


def getLinks(html, bsObj):
    tag_list = bsObj.find("div", {"class":"poster_container"}).findAll("a", href=re.compile("(/m/)((?!:).)*$"))
    for tag in tag_list:
        if 'href' in tag.attrs:
            f.write(str(tag.attrs['href']) + "\n")
        else:
            f.write("no href\n")

getLinks(html, bsObj)
f.close()
