import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    xbmc.log('type: %s'%(type(soup)),xbmc.LOGDEBUG)
    print("type: ", type(soup))
    return soup
get_soup("http://www.americanmythologypodcast.com/episodes?format=RSS")

def get_playable_podcast(soup):
    subjects = []
    for content in soup.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'Link': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://images.squarespace-cdn.com/content/5671a4705a5668ba6b111b2b/1481812482959-FT137O7ZRUC6ERWMRA0R/AMLogo-1400x1400.png"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast(playable_podcast):
    items = []
    for podcast in playable_podcast:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['Link'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

def get_playable_podcast1(soup):
    subjects = []
    for content in soup.find_all('item', limit=9):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            desc = content.find('itunes:subtitle')
#            desc = desc.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'Link': link,
                'title': title,
#                'desc': desc,
                'thumbnail': "https://images.squarespace-cdn.com/content/5671a4705a5668ba6b111b2b/1481812482959-FT137O7ZRUC6ERWMRA0R/AMLogo-1400x1400.png"
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
#            'info': podcast['desc'],
            'is_playable': True,
    })
    return items

