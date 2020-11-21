import requests
from bs4 import BeautifulSoup

from .abstract import PickuplineAbstract

class Pickuplinegen(PickuplineAbstract):
    
    @property
    def source_url(self):
        return "http://www.pickuplinegen.com/"

    def extract(self):
        resp = requests.get(self.source_url)
        if resp.status_code != 200:
            raise Exception("Error in fetching response from {}".format(self.source_url))
        soup = BeautifulSoup(resp.content, "html5lib")
        return soup.select("body > section > div#content")[0].text.strip()

    def get_pickupline(self, random=True):
        return self.extract()


