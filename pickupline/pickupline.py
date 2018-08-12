from __future__ import print_function
import requests
from bs4 import BeautifulSoup
import sys
import random as Random


def get_soup(url):
    try:
        return BeautifulSoup(requests.get(url).text,"html5lib")
    except Exception as SockException:
        print(SockException)
        sys.exit(1)

class PickupLine(object):
    def __init__(self, random=None, geek=None, dirty=None, math=None, physics=None, scifi=None):
        """
        attrs: `random`,`geek`,`dirty`,`math`,`physics`,`scifi`
        set attributes for required PickupLine 
        i.e PickupLine(geek=True)
        """
        self.random = False
        self.url = "http://www.pickuplinesgalore.com/"
        if geek:
            self.url += "computer.html"
        elif dirty:
            self.url += "crude.html"
        elif math:
            self.url += "math.html"
        elif physics:
            self.url += "physics.html"
        elif scifi:
            self.url += "scifi.html"
        else:
            self.random = True
            self.url = "http://www.pickuplinegen.com/"
    def get_line(self):
        """
        e.g PickupLine(geek=True).get_line() will
        return a geeky pickupline
        """
        if self.random:
            return get_soup(self.url).select("body > section > div#content")[0].text.strip()
        else:
            soup = get_soup(self.url)
            lines = "\n".join([i.text.strip() for i in soup.select("main > p.action-paragraph.paragraph > span") if "<<" not in i.text.strip()])
            lines = [line.strip() for line in lines.split("\n") if line.strip()]
            return lines[Random.randrange(0,len(lines)-2)].strip()



