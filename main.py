# WikiLinkScrapper- this program is a web scraper designed to enter a word in wikipedia
# and follow the first x number of links to other wikipedia pages.
# I think it would be amusing to see where it ends up.

import requests
from bs4 import BeautifulSoup
import random


url_list = []
# You can select desired parameter below
# Note that " " must be enter as "_". Thus, "Steve Jobs" would be "Steve_Jobs"
Wikipage= "Steve_Jobs"
Number_O_Searches = 10
Link_Number = 2




# fetches all links on the content page of the given "Wikipage" root page.
# "Wikipage" is a variable above
url = ("/wiki/" + Wikipage)
for x in range(Number_O_Searches):
    r = requests.get("https://en.wikipedia.org" + url)
    b = BeautifulSoup(r.text, "html.parser")
    b = b.find("div", class_="mw-parser-output").findAll("p")
    list_O_links = []
    for a in b:
        for b in a.findAll("a"):
            #print(b["href"]) This can be used to print all the links found
            if str(b["href"]).find("#") == -1 and str(b["href"]).find(".") == -1 and str(b["href"]).find(":") == -1:
                list_O_links.append(b["href"])
                #print(list_O_links) This filters out the links that are undesired

    #for x in list_O_links:   # unmuting this will print all links found on this page that are links to other wikipedia pages. 
        #print(x)

    #Wikipedia seems to keep falling into a loop. Everything below is to avoid that.
    link_number = Link_Number
    url = list_O_links[link_number]
    if url in url_list:
        rand = random.choice(range(len(list(b))))
        if rand != link_number:
            url = list_O_links[rand]
    url_list.append(url)
    print("\n" + url)