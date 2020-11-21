import random
import os

import requests
from bs4 import BeautifulSoup

from .abstract import PickuplineAbstract
from .cache import cache_to_disk, DiskCache
from .constants import PICKUPLINE_CONFIG_DIR


CONFIG_FILEPATH = os.path.join(PICKUPLINE_CONFIG_DIR, "pickuplinesgalore.json")

CATEGORY_CACHE_KEY = "{}-results"
LIST_OF_CATEGORIES_CACHE_KEY = "categories-list"

class PickuplinesGalore(PickuplineAbstract):    
    
    def __init__(self, keyword=None):
        self.keyword = keyword
        self.cache = DiskCache(CONFIG_FILEPATH)

    @property
    def source_url(self):
        return "https://www.pickuplinesgalore.com/"

    def clean_line(self, line):
        return "\n".join(filter(lambda x: len(x.strip()) > 0, line.split("\n")))

    def get_list_of_categories(self):
        return self.cache.get(LIST_OF_CATEGORIES_CACHE_KEY) or []

    def parse_category(self, category, category_url):
        cat_cache_key = CATEGORY_CACHE_KEY.format(category)
        if self.cache.get(cat_cache_key) and self.cache.last_modified_days_ago < 100:
            return self.cache.get(cat_cache_key)
        resp = requests.get(category_url)
        if resp.status_code != 200:
            raise Exception("Error in fetching from {}".format(self.source_url))
        soup = BeautifulSoup(resp.content, "html5lib")
        lines = "\n".join([self.clean_line(line.text.strip()) for line  in soup.select("main > p.action-paragraph.paragraph > span")])
        result = [line.strip() for line in lines.split("\n") if line.strip()]
        self.cache.set(cat_cache_key, result)
        return result

    @cache_to_disk(CONFIG_FILEPATH)
    def _parse_index_page(self):
        resp = requests.get(self.source_url)
        if resp.status_code != 200:
            raise Exception("Error in fetching from {}".format(self.source_url))
        soup = BeautifulSoup(resp.content, "html5lib")
        a_tags = soup.findAll("a", {"class":"responsive-picture picture-link-1"})
        data = self.cache.get_json_data()
        categories = []
        for tag in a_tags:
            category_url = tag.attrs.get("href")
            category = category_url.replace(".html","")
            data[category] = self.source_url + category_url
            categories.append(category)
        data[LIST_OF_CATEGORIES_CACHE_KEY] = categories
        return data

    def parse_index_page(self):
        if self.cache.is_empty() or self.cache.last_modified_days_ago > 100:
            return self._parse_index_page()
        return self.cache.get_json_data()

    def search(self, keyword):
        data = self.parse_index_page()
        for category in data.keys():
            # TODO: Implement fuzzy matching
            if keyword in category:
                return self.parse_category(category, data[category])
        return []

    def get_pickupline(self, keyword):
        lines = self.search(keyword.lower())
        if lines:
            return lines[random.randrange(0,len(lines)-2)]