import os

import requests
from colorama import Fore
from pygments.styles.paraiso_light import YELLOW

os.system('cls')


class bcolors:
    Black = '\033[30m'
    Redd = "\033[31m"
    Greenn = "\033[32m"
    Yelloww = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"


usuario = input('\033[92m{+} Insira o usuário: ')

# insta
instagram = f'https://www.instagram.com/{usuario}'

# facebook
facebook = f'https://www.instagram.com/{usuario}'

# twitter
twitter = f'https://www.twitter.com/{usuario}'

# youtube
youtube = f'https://www.youtube.com/{usuario}'

# blog
blogger = f'https://{usuario}.blogspot.com'

# Google +
google_plus = f'https://plus.google.com/s/{usuario}top'

# reddit
reddit = f'https://www.reddit.com/user/{usuario}'

# Wordpress
wordpress = f'https://{usuario}.wordpress.com'

# PINTEREST
pinterest = f'https://www.pinterest.com/{usuario}'

# GITHUB
github = f'https://www.github.com/{usuario}'

# TUMBLR
tumblr = f'https://{usuario}.tumblr.com'

# FLICKR
flickr = f'https://www.flickr.com/people/{usuario}'

# STEAM
steam = f'https://steamcommunity.com/id/{usuario}'

# VIMEO
vimeo = f'https://vimeo.com/{usuario}'

# SOUNDCLOUD
soundcloud = f'https://soundcloud.com/{usuario}'

# DISQUS
disqus = f'https://disqus.com/by/{usuario}'

# MEDIUM
medium = f'https://medium.com/@{usuario}'

# DEVIANTART
deviantart = f'https://{usuario}.deviantart.com'

# VK
vk = f'https://vk.com/{usuario}'

# ABOUT.ME
aboutme = f'https://about.me/{usuario}'

# IMGUR
imgur = f'https://imgur.com/user/{usuario}'

# FLIPBOARD
flipboard = f'https://flipboard.com/@{usuario}'

# SLIDESHARE
slideshare = f'https://slideshare.net/{usuario}'

# FOTOLOG
fotolog = f'https://fotolog.com/{usuario}'

# SPOTIFY
spotify = f'https://open.spotify.com/user/{usuario}'

# MIXCLOUD
mixcloud = f'https://www.mixcloud.com/{usuario}'

# SCRIBD
scribd = f'https://www.scribd.com/{usuario}'

# BADOO
badoo = f'https://www.badoo.com/en/{usuario}'

# PATREON
patreon = f'https://www.patreon.com/{usuario}'

# BITBUCKET
bitbucket = f'https://bitbucket.org/{usuario}'

# DAILYMOTION
dailymotion = f'https://www.dailymotion.com/{usuario}'

# ETSY
etsy = f'https://www.etsy.com/shop/{usuario}'

# CASHME
cashme = f'https://cash.me/{usuario}'

# BEHANCE
behance = f'https://www.behance.net/{usuario}'

# GOODREADS
goodreads = f'https://www.goodreads.com/{usuario}'

# INSTRUCTABLES
instructables = f'https://www.instructables.com/member/{usuario}'

# KEYBASE
keybase = f'https://keybase.io/{usuario}'

# KONGREGATE
kongregate = f'https://kongregate.com/accounts/{usuario}'

# LIVEJOURNAL
livejournal = f'https://{usuario}.livejournal.com'

# ANGELLIST
angellist = f'https://angel.co/{usuario}'

# LAST.FM
last_fm = f'https://last.fm/user/{usuario}'

# DRIBBBLE
dribbble = f'https://dribbble.com/{usuario}'

# CODECADEMY
codecademy = f'https://www.codecademy.com/{usuario}'

# GRAVATAR
gravatar = f'https://en.gravatar.com/{usuario}'

# PASTEBIN
pastebin = f'https://pastebin.com/u/{usuario}'

# FOURSQUARE
foursquare = f'https://foursquare.com/{usuario}'

# ROBLOX
roblox = f'https://www.roblox.com/user.aspx?username={usuario}'

# GUMROAD
gumroad = f'https://www.gumroad.com/{usuario}'

# NEWSGROUND
newsground = f'https://{usuario}.newgrounds.com'

# WATTPAD
wattpad = f'https://www.wattpad.com/user/{usuario}'

# CANVA
canva = f'https://www.canva.com/{usuario}'

# CREATIVEMARKET
creative_market = f'https://creativemarket.com/{usuario}'

# TRAKT
trakt = f'https://www.trakt.tv/users/{usuario}'

# 500PX
five_hundred_px = f'https://500px.com/{usuario}'

# BUZZFEED
buzzfeed = f'https://buzzfeed.com/{usuario}'

# TRIPADVISOR
tripadvisor = f'https://tripadvisor.com/members/{usuario}'

# HUBPAGES
hubpages = f'https://{usuario}.hubpages.com'

# CONTENTLY
contently = f'https://{usuario}.contently.com'

# HOUZZ
houzz = f'https://houzz.com/user/{usuario}'

# BLIP.FM
blipfm = f'https://blip.fm/{usuario}'

# WIKIPEDIA
wikipedia = f'https://www.wikipedia.org/wiki/User:{usuario}'

# HACKERNEWS
hackernews = f'https://news.ycombinator.com/user?id={usuario}'

# CODEMENTOR
codementor = f'https://www.codementor.io/{usuario}'

# REVERBNATION
reverb_nation = f'https://www.reverbnation.com/{usuario}'

# DESIGNSPIRATION
designspiration = f'https://www.designspiration.net/{usuario}'

# BANDCAMP
bandcamp = f'https://www.bandcamp.com/{usuario}'

# COLOURLOVERS
colourlovers = f'https://www.colourlovers.com/love/{usuario}'

# IFTTT
ifttt = f'https://www.ifttt.com/p/{usuario}'

# EBAY
ebay = f'https://www.ebay.com/usr/{usuario}'

# SLACK
slack = f'https://{usuario}.slack.com'

# OKCUPID
okcupid = f'https://www.okcupid.com/profile/{usuario}'

# TRIP
trip = f'https://www.trip.skyscanner.com/user/{usuario}'

# ELLO
ello = f'https://ello.co/{usuario}'

# TRACKY
tracky = f'https://tracky.com/user/~{usuario}'

# BASECAMP
basecamp = f'https://{usuario}.basecamphq.com/login'

SITES = [
    instagram, facebook, twitter, youtube, blogger, google_plus, reddit,
    wordpress, pinterest, github, tumblr, flickr, steam, vimeo, soundcloud, disqus,
    medium, deviantart, vk, aboutme, imgur, flipboard, slideshare, fotolog, spotify,
    mixcloud, scribd, badoo, patreon, bitbucket, dailymotion, etsy, cashme, behance,
    goodreads, instructables, keybase, kongregate, livejournal, angellist, last_fm,
    dribbble, codecademy, gravatar, pastebin, foursquare, roblox, gumroad, newsground,
    wattpad, canva, creative_market, trakt, five_hundred_px, buzzfeed, tripadvisor, hubpages,
    contently, houzz, blipfm, wikipedia, hackernews, reverb_nation, designspiration,
    bandcamp, colourlovers, ifttt, ebay, slack, okcupid, trip, ello, tracky, basecamp,
]

''' impressao de cores'''


def outer_func(colour):
    def inner_function(msg):
        print(f'{colour}{msg}')

    return inner_function


'''impressão de cores'''

''' R4 D0xing banner '''


def banner():
    print(Fore.LIGHTBLUE_EX + '''     .'|
             |  |  _ _
             |  | (_X_)
             |  |   |
              `.|_.-"-._
                |.-"""-.|
               _;.-"""-.;_
           _.-' _..-.-.._ '-._
          ';--.-(_o_I_o_)-.--;'
           `. | |  | |  | | .`
             `-\|  | |  |/-'
                |  | |  |
                |  \_/  |
             _.'; ._._. ;'._
        _.-'`; | \  -  / | ;'-.
      .' :  /  |  |   |  |  \  '.
     /   : /__ \  \___/  / __\ : `.
    /    |   /  '._/_\_.'  \   :   `\
   /     .  `---;"""""'-----`  .     \
  /      |      |()    ()      |      \
 /      /|      |              |\      \
/      / |      |()    ()      | \      \
|         |
\     \  | ][     |   |    ][  |  /     /
 \     \ ;=""====='"""'====""==; /     /
  |/`\  \/      |()    ()      \/  /`\|
   |_/.-';      |              |`-.\_|
     /   |      ;              :   \
     |__.|      |              |.__|
         ;      |              |
         |      :              ;
         |      :              |
         ;      |              |
         ;      |              ;
         |      :              |
         |      |              ;
         |      |              ;
         '-._   ;           _.-'
             `;"--.....--";`
              |    | |    |
              |    | |    |
              |    | |    |
              T----T T----T
         _..._L____J L____J _..._
       .` "-. `%   | |    %` .-" `.
      /      \    .: :.     /      \
      '-..___|_..=:` `-:=.._|___..-'  ''')


def search():
    import time
    time.sleep(0.5)
    print(Fore.LIGTHORANGE_EX + f' [🕵️‍♂️] Busque o nome do usuário :{usuario}')
    time.sleep(0.5)
    print('████████')

    time.sleep(0.5)

    print('████████')
    time.sleep(0.5)

    print(Fore.LIGHTMAGENTA_EX + "[+] R4 Doxing iniciando ")

    time.sleep(0.5)

    print('████████')

    time.sleep(0.5)

    time.sleep(1)

    count = 0

    match = True
    for url in SITES:
        r = requests.get(url)

        if r.status_code == 200:
            if match:
                print(Fore.LIGHTYELLOW_EX + '[+] Resultados')
                match = False
                YELLOW(f'\n{url} - {r.status_code} - OK')
                if usuario in r.text:
                    print(
                        Fore.LIGHTGREEN_EX + f'[r4 d0xing] POSITIVO: Nome do usuário :{usuario} Este nome foi '
                                             f'detectado nessa URL')
                else:
                    print(
                        Fore.LIGHTRED_EX + f'[r4 d0xing] NEGATIVO: Nome do usuario:{usuario} -\033[91m r4 d0xing não '
                                           f'foi capaz de detectar nessa URL,digite corretamente se persistir')
                count += 1

            total = len(SITES)
            print(Fore.LIGHTCYAN_EX + f'Terminado: Total de {count} contas encontradas {total} sites')

            print(bcolors.Redd + 'teste')

        if __name__ == '__main__':
            banner()
            search()
