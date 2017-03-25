import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from random import randint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import csv

driver = webdriver.Chrome('/Users/haileyanderton/Documents/python/scraping/chromedriver')
driver.get('https://www.rottentomatoes.com/browse/dvd-all/?minTomato=80&services=amazon;amazon_prime;fandango_now;hbo_go;itunes;netflix_iw;vudu');

# open new file for writing
csvfile = open("rotten_tomatoes.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
# write the header row in the CSV
c.writerow(['title', 'tomatometer', 'rating', 'released', 'genre', 'runtime'])

# my path is '/Users/haileyanderton/Documents/python/scraping/chromedriver'

# click the button exactly 151 times to get all 4826 titles

#def load_page(html, bsObj):
for n in range(10):
    driver.find_element_by_css_selector('.btn.btn-secondary-rt.mb-load-btn').click()
    # make a random wait time between 1 and 10 seconds to look less bot-like
    s = randint(1, 12)
    time.sleep(s)
    print("scrolling and clicking!")

#load_page(html, bsObj)

html = driver.page_source
bsObj = BeautifulSoup(html, "html.parser")
movie_list = []
data = bsObj.findAll('div', {'class':'movie_info'})
for div in data:
    links = div.findAll('a')
    for a in links:
        movie_list.append(str(a.attrs['href']))

#get_movie_links(html, bsObj)

def get_movie_details(movie_list):
    counter = 0
    for movie in movie_list:
        new_url = "https://www.rottentomatoes.com" + movie
        html = urlopen(new_url)
        bsObj = BeautifulSoup(html, "html.parser")
        movie_details = []
        title = bsObj.find( "h1", {"id":"movie-title"} )
        # div class title (text) player's full name
        tomatometer = bsObj.find("span", {"class":"meter-value superPageFontColor"}).find("span")
            # div class club (text) team
        rating = bsObj.find('div', text = re.compile("(^.*(R|P|G)(?:...)).*$"), attrs = {'class' : 'meta-value'})
            # div class position (text) position
        release_year = bsObj.find( "span", {"class":"h3 year"} )
            # <div class="age"><span class="category">Age:</span>
            # 23 (10/21/1992)</div>
        genre = bsObj.find('a', href=re.compile(".*(/browse/opening/\?genres).*"))
            # <div class="hometown"><span class="category">Birthplace:</span>
            # Barranquilla, Colombia</div>
        runtime = bsObj.find('time', text = re.compile(".*(minutes).?"))

        row = []
            # <div class="twitter_handle"><a
            # href="https://twitter.com/Olmesgarcia13"
            # class="twitter_link">@Olmesgarcia13</a></div>
            #score = tomatometer.findAll("span")
            #print(score + '%')
            # need to get_text
            # need to add delay
        movie_details = [title, tomatometer, rating, release_year, genre]
        for detail in movie_details:
            try:
                # write a new item into the list, row
                row.append( detail.get_text() )
            except AttributeError:
                # write a new item into the list, row
                row.append( "None" )

        # write a new row in the CSV, by writing the list
        c.writerow( row )

        counter += 1

        # let me know how far along it is
        if counter == 250:
            print("250, almost done...")
        elif counter == 200:
            print("200 plus ...")
        elif counter == 150:
            print("150 plus ...")
        elif counter == 100:
            print("100 plus ...")
        elif counter == 50:
            print("50 plus ...")


        if counter % 10 == 0:
            time.sleep(1)


get_movie_details(movie_list)

csvfile.close()

driver.quit()

print("Yay, done!")
