import os

import bs4
import requests
import cv2
import numpy as np


def getComic():
    os.makedirs('comics', exist_ok=True)
    res = requests.get('http://explosm.net/rcg')
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    comic_url = 'http://' + soup.select('#rcg-comic img')[0].attrs['src'][2:]
    comic_res = requests.get(comic_url)
    comic_name = comic_url.split('/')[-1]
    comic_file = open('comics/' + comic_name, 'wb')
    for chunk in comic_res.iter_content(100000):
        comic_file.write(chunk)
    comic_file.close()
    return comic_name


def getPanels(comic_name):
    img = cv2.imread('comics/' + comic_name)
    height, width, channels = img.shape
    img0 = img[5:height - 14, 5:int(width / 3) - 7]
    height0, width0, channels = img0.shape
    img0[height0 - 18:height0, width0 - 34:width0] = [255, 255, 255]
    img1 = img[5:height - 14, int(width / 3) * 2 + 8:width - 5]
    height1, width1, channels = img1.shape
    img1[height1 - 18:height1, 0:34] = [255, 255, 255]
    cv2.imwrite('comics/' + comic_name.split('.')[0] + '_0.' + comic_name.split('.')[1], img0)
    cv2.imwrite('comics/' + comic_name.split('.')[0] + '_1.' + comic_name.split('.')[1], img1)
    os.unlink('comics/' + comic_name)
    return comic_name


if __name__ == "__main__":
    for i in range(0, 5):
        getPanels(getComic())
