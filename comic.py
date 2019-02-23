import os

import bs4
import requests


def getComic():
    os.makedirs('comics', exist_ok=True)
    res = requests.get('http://explosm.net/rcg')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)
    comic_url = 'http://' + soup.select('#rcg-comic img')[0].attrs['src'][2:]
    comic_res = requests.get(comic_url)
    comic_name = comic_url.split('/')[-1]
    comic_file = open('comics/' + comic_name, 'wb')
    for chunk in comic_res.iter_content(100000):
        comic_file.write(chunk)
    comic_file.close()
    return comic_name


if __name__ == "__main__":
    getComic()
