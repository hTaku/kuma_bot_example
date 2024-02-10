import requests
from scrapings import Scraping
from line import Line
import settings

def _convertLinePost(entry):
    return entry[0] + '\n\n' + entry[2]  + '\n\n' + '日時: ' + entry[1]

if __name__ == "__main__":
    entries = Scraping().get_kama('熊')
    line = Line(settings.ACCESS_TOKEN)
    if entries.__len__ != 0:
        post = _convertLinePost(entries[0])
        line.post_notify(post)
