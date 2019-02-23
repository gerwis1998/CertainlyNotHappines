from distutils.core import setup
import py2exe

setup(console=['comic.py'], requires=['urllib3', 'requests', 'beautifulsoup4', 'cv2'])
