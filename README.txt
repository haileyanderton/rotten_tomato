Rotten Tomatoes Webscraper

The Proposal

My original proposal was to scrape the movies rated 80% or higher on the tomatometer on Rotten Tomatoes for their title, tomatometer rating, rating (G, PG, etc.), release date, genre and runtime. I have partially accomplished that, except that I could only retrieve 158 of the 4800+ movies that I needed to scrape. My theory is that either 1. something from my computer was disrupting the scrape or, more likely, Rotten Tomatoes was blocking me from scraping because they thought I was a bot. Anyhow, here's how I did it:

Step 1

First, I needed to extract all of the URLs for the webpages of the movie titles, so that I could then extract the data I wanted from there. I looked through the developer tools on the page a few weeks prior and saw recognizable tags and attributes, so I thought this would be pretty simply. I was WRONG.

Challenge 1

It turns out Rotten Tomatoes was using Javascript to hide the html, making it impossible to scrape. So, with my professor's help, I downloaded Selenium, which renders the page so I could scrape it! Download links:

http://selenium-python.readthedocs.io/installation.html

http://selenium-python.readthedocs.io/installation.html#drivers

Challenge 2

Next, I had to tackle another problem: executing the "see more" button on the page to get all 4800 links. The problem with this particular button was that it did not have an id or a link to identify it with. The only way to get it to work was by using the find_element_by_css_selector command in Selenium that selected the class of the button and used the .click() command to click on it. Ideally, this would have to be clicked 151 times to have all 4800 links revealed on the page.

Step 2

Now, with everything revealed, I could scrape the URLs to the individual movie pages. I just pushed the button 3 times to start to make testing faster, and got it to scrape and print all of the URLs, and put them in an empty list.

Step 3

Next, I used that list of URLs as an argument in a function that scraped those individual pages for the movie details I was looking for. I used a lot of regex to find the specific details because the html was not well-marked and it was difficult to differentiate one tag from another. When I extracted all of the individual details I wanted, they were then placed into another list and eventually printed into rows in a csv file. This was all contained in a function I named get_movie_details()

Conclusion

Overall, I am satisfied with all that I learned and happy that I persevered the many frustrating moments of this project. I definitely look forward to getting it to work properly in the future!

Here are some tutorials/resourced that I used to help me along the way:

regex structure:
http://stackoverflow.com/questions/9007653/how-to-find-tag-with-particular-text-with-beautiful-soup
pythex.org

selenium help:
http://stackoverflow.com/questions/35111853/selenium-python-click-button?rq=1
https://automatetheboringstuff.com/chapter11/
