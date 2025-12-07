import asyncpraw
from dhooks import Webhook

# Note that for this file, if there are apostrophes present fill this out BETWEEN them.

# MLR ONLY: go to the current MLR roster sheets (NOT MiLR, regardless of which league you are running it for). 
# For SHEET, copy/paste this part of the URL: https://docs.google.com/spreadsheets/d/ -- COPY PASTE THIS -- /edit
# For TAB, put the name of the tab that stores player names and MLR team, but replace any spaces with "%20".
# As of Session 12.1, this should be written as "Player%20List".
SHEET = '1XDz5kZTf8S48w2YmYL0rmstmf52wdXG3JECMaSBV5yQ'
TAB = 'Player%20List'

# asyncpraw = Asynchronous Python Reddit API Wrapper
# go to https://www.reddit.com/prefs/apps
# hit "create an app..." at the bottom
# fill in the form. hit "script" for the bubbles. fill in literally anything for the rest, it does not matter
# you will see the name of your bot, then "personal use script", then your **client_id**. copy/paste this below.
# below this (hit "edit" if it's hidden) you should see your **client_secret**. copy/paste this below.
# name user_agent literally anything; it again doesn't matter.

async def setup_reddit():
    reddit = asyncpraw.Reddit(
        client_id     = '',
        client_secret = '',
        user_agent    = 'RSS'
    )
    
    return reddit

# List of players who do *not* want to be pinged. This should be in the following format:
# ping_exclude = ['Stupido Einsteiny', 'Mark Schihne']
ping_exclude = []

# how many hours before the end of the timer would you like to be notified?
before_end = 4

# List of RSS feeds for each league. Delete those you don't need and modify those you do, while maintaining the formatting.
# To get the webhook: go to server settings, then integrations, then webhooks
# create a new webhook. name it, pick what channel you want it in, and then hit the "copy webhook URL" button and paste it below.
rss_feeds = [
    {
        'search'  : 'Oakland Athletics', # The program looks for new comments in posts with this in the title.
        'abbrev'  : 'OAK', # Your team abbreviation.
        'webhook' : Webhook(''),
        'hexcode' : '003831', # The color of the vertical bar on the side (you choose)
        'results' : True, # True: you want to see the bot's result comments (in addition to the MLR webhook), False: you do not
        'ping'    : True, # True: your team wants pings (they can be disabled at the individual level). False: nobody wants pings
        'timer'   : {'need ping' : False, 'snowflake' : None, 'end' : None}, # NO TOUCHY TOUCHY
        'leaders' : ['Six', 'Teddy Bigstick', 'Mark Schihne', 'Total Dial'] # in addition to the hitter, who is pinged when timer runs low
    },
    {
        'search'  : 'Kier Goats',
        'abbrev'  : 'KEG',
        'webhook' : Webhook(''),
        'hexcode' : '40B4E7',
        'results' : False,
        'ping'    : True,
        'timer'   : {'need ping' : False, 'snowflake' : None, 'end' : None},
        'leaders' : ["Archie 'Clumsy' Sybil", "Kordz Sonata", "Laars Nootbaar jr", "Arthur Bullpendragon"]
    }
]