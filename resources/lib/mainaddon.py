import requests
import re
from bs4 import BeautifulSoup

def get_soup(url):
    """
    @param: url of site to be scraped
    """
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
#    xbmc.log('type: %s'%(type(soup)),xbmc.LOGDEBUG)
    
    print("type: ", type(soup))
    return soup

get_soup("http://www.americanmythologypodcast.com/episodes")


def get_playable_podcast(soup):
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('div'):
        
        try:        
            link = content.find({'class': 'data-url'})
            link = link.get()
            print("\n\nLink: ", link)

            title = content.find({'class': 'title-url'})
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
                'thumbnail': "resources/media/icon.png"
        }
        
        subjects.append(item) 
    
    return subjects




def compile_playable_podcast(playable_podcast):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
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
    """
    @param: parsed html page            
    """
    subjects = []

    for content in soup.find_all('div', limit=5):
        
        try:        
            link = content.find({'class': 'data-url'})
            link = link.get()
            print("\n\nLink: ", link)

            title = content.find({'class': 'title-url'})
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
                'thumbnail': "resources/media/icon.png"
        }
        
        subjects.append(item) 
    
    return subjects


def compile_playable_podcast1(playable_podcast1):
    """
    @para: list containing dict of key/values pairs for playable podcasts
    """
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

