import xbmc
#from kodi_six import xbmc, xbmcaddon, xbmcgui, xbmcplugin, xbmcvfs
#from xbmc import Plugin, xbmcgui
from xbmcswift2 import Plugin, xbmcgui
#from kodi_six import Plugin
from resources.lib import mainaddon

URL = "http://www.americanmythologypodcast.com/episodes?format=RSS"
plugin = Plugin()
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('all_episodes1'),
            'thumbnail': "https://images.squarespace-cdn.com/content/5671a4705a5668ba6b111b2b/1481812482959-FT137O7ZRUC6ERWMRA0R/AMLogo-1400x1400.png"},
        {
            'label': plugin.get_string(30000), 
            'path': plugin.url_for('all_episodes'),
            'thumbnail': "https://images.squarespace-cdn.com/content/5671a4705a5668ba6b111b2b/1481812482959-FT137O7ZRUC6ERWMRA0R/AMLogo-1400x1400.png"},
    ]
    return items

@plugin.route('/all_episodes1/')
def all_episodes1():
    soup = mainaddon.get_soup(URL)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/all_episodes/')
def all_episodes():
    soup = mainaddon.get_soup(URL)
    playable_podcast = mainaddon.get_playable_podcast(soup)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
