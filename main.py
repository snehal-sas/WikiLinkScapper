# WikiLinkScrapper- this program is a web scraper designed to enter a word in wikipedia
# and follow the first x numbered link to other wikipedia pages y number of times.
# I think it would be amusing to see where it ends up.

import requests
from bs4 import BeautifulSoup
import random


url_list = []
# You can select desired parameter below
# Note that " " must be enter as "_". Thus, "Steve Ballmer" would be "Steve_Ballmer"
Wikipage= "Steve_Ballmer"
Number_O_Searches = 7
Link_Number = 5  
# fetches all links on the content page of the given "Wikipage" root page


url = ("/wiki/" + Wikipage)
Link_Number = Link_Number - 3
for x in range(Number_O_Searches):
    r = requests.get("https://en.wikipedia.org" + url)
    b = BeautifulSoup(r.text, "html.parser")
    b = b.find("div", class_="mw-parser-output").findAll("p")
    list_O_links = []
    for a in b:
        for link in a.findAll("a"):
            #print(link["href"]) # This can be used to print all the links found
            # this if statement exists to filter out links that are citations links and not other wikipedia pages.
            if (str(link["href"]).find("#") == -1 and str(link["href"]).find(".") == -1 and str(link["href"]).find(":") == -1):
                list_O_links.append(link["href"])
                

    #for x in range(7):   # unmuting this will print all links found on this page that are links to other wikipedia pages. 
        #print(list_O_links[x])

    #Wikipedia seems to keep falling into a loop. Everything below is to avoid that.
    url = list_O_links[Link_Number+1]
    updated_link_number = Link_Number +1
    while True:
        if url in url_list:
            updated_link_number = updated_link_number + 1
            url = list_O_links[updated_link_number]
        else:
            break
    url_list.append(url)
    print("\n" + url)