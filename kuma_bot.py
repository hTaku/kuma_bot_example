import requests
from scraping import Scraping
from line import Line

def _convertLinePost(entry):
    return entry[0] + '\n\n' + entry[2]  + '\n\n' + '日時: ' + entry[1]

if __name__ == "__main__":
    entries = Scraping().get_kama('熊')
    line = Line('KQMwuQy8qzOs6xZ3kG3Mek8pmp9ziqs3zwv3Wb6bTk8')
    if entries.__len__ != 0:
        post = _convertLinePost(entries[0])
        line.post_notify(post)
