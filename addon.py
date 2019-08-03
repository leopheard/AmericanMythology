import xbmc
#from kodi_six import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs
#from xbmc import Plugin, xbmcgui
from xbmcswift2 import Plugin, xbmcgui
#from kodi_six import Plugin
from resources.lib import mainaddon

URL = "http://www.americanmythologypodcast.com/episodes"

plugin = Plugin()

@plugin.route('/')
def main_menu():
    """
    main menu 
    """
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "resources/media/icon.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "resources/media/icon.png"},
    ]

    return items

@plugin.route('/all_episodes/')
def all_episodes():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast = mainaddon.get_playable_podcast(soup)
    
    items = mainaddon.compile_playable_podcast(playable_podcast)

    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    """
    contains playable podcasts listed as just-in
    """
    soup = mainaddon.get_soup(URL)
    
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    
    items = mainaddon.compile_playable_podcast1(playable_podcast1)

    return items

if __name__ == '__main__':
    plugin.run()
