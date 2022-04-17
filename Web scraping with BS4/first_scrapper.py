# scrapper for https://quotes.toscrape.com/

from ast import parse
import requests
from bs4 import BeautifulSoup

page = requests.get("https://quotes.toscrape.com/")

#HTML parser


if page.status_code == 200:
    
    
    ### --- BASICS
    
    ##-- HTML Selector
    
    
    # lxml is the best and faster
    parsed_page = BeautifulSoup(page.content,'lxml')
    
    # html5 is better when html to parse is not well formatted
    #parsed_page = BeautifulSoup(page.content,'html.parser')
    
    # the base avec beactiful soup, la plus lente mais la plus sure
    #parsed_page = BeautifulSoup(page.content,'html5lib')
    
    #print(parsed_page)
    
    
    #we can get 'importants' tags like body and head like this
    #parsed_page.title
    #parsed_page.head
    #parsed_page.body
    
    #print(parsed_page.h2)
    
    
    ### --- FIND
    bouton_next = parsed_page.find('li',{'class':'next'})
    print(bouton_next)
    
    
    #top_ten_tags = parsed_page.find('div',{'class':'col-md-4 tags-box'})
    #print(top_ten_tags)
    
    
    # get all links a list
    #link_list = parsed_page.find_all('a')
    #print(link_list)
    
    
    
    # get allo quotes link
    
    #quotes = parsed_page.find_all('span',{'class':'text'})
    #print(quotes)
    
    
    # parsing blocks
    top_ten_tags = parsed_page.find('div',{'class':'col-md-4 tags-box'})
    top_ten_tags_list = top_ten_tags.find_all('a',{'class':'tag'})
    
    # use this code to parse blocks faster but is not to clear
    #top_ten_tags_list = parsed_page.find('div',{'class':'col-md-4 tags-box'}).find_all('a',{'class':'tag'})
    
    print(top_ten_tags_list)
    
    #for tag in top_ten_tags_list:
        # attirbutes
        #print(tag.attrs)
        #print(tag.string)
        
        
    
    # get text directly from tag
    print(parsed_page.h1.get_text())
    
    
    ### --- GET AND STORE DATA
    
    
    #quotes = parsed_page.find_all('span',{'class':'text'})
    quotes_list = []
    #for quote in quotes:
    #    quotes_list.append(quote.string)
    #print(quotes_list)    
    
    # the same but faster 
    quotes_list = [quote.string for quote in quotes_list]
    print(quotes_list)
    
    
    ## --- CSS SELECTOR
    
    print(parsed_page.select("title"))
    
    # when we get data, we get it into a list because selector function make a list of each tag found in html
    
    
    # we can select child elements in one line thought selector
    print(parsed_page.select("span a")) # get all <a> tags into <span> tags
    
    
    # get thought class
    print(parsed_page.select(".tag"))
    
    
    # get all tags that contain a specific string
    print(parsed_page.select("a[href='/tag/inspirational/page/1/']"))
    
    
    
    
    
    
    
    
    
    
    
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    