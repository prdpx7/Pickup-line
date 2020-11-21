import json
import os
from datetime import datetime

class DiskCache:
    """
    A wrapper class to handle cache get/set on disk
    """

    def __init__(self, config_filepath):
        self.config_filepath = config_filepath
        self.config_dir = os.path.dirname(self.config_filepath)
        self.last_modified_at = None
        self.last_modified_days_ago = None
        # create config directory
        if not os.path.exists(self.config_dir):
            os.mkdir(self.config_dir)
        self.update_config_file_stat()

    def update_config_file_stat(self):
        if os.path.exists(self.config_filepath):
            last_modified_time = os.path.getmtime(self.config_filepath)
            self.last_modified_at =  datetime.fromtimestamp(last_modified_time)
            self.last_modified_days_ago = (datetime.now() - self.last_modified_at).days

    def is_empty(self):
        return True if self.last_modified_at is None else False
    
    def get_json_data(self):
        if not os.path.exists(self.config_filepath):
            return {}
        with open(self.config_filepath, "r") as fp:
            return json.load(fp)

    def set_json_data(self, data):
        # overwrite everything in config_filepath with incoming data
        with open(self.config_filepath, "w") as fp:
            json.dump(data, fp)
        self.update_config_file_stat()
        
    def get(self, key):
        data = self.get_json_data()
        return data.get(key)

    def set(self, key, val):
        data = self.get_json_data()
        data[key] = val
        self.set_json_data(data)


def cache_to_disk(config_filepath):
    """
    Decorator to cache json results of funcs on a given filepath
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            data = func(*args, **kwargs)
            cache = DiskCache(config_filepath)
            cache.set_json_data(data)
            return data
        return wrapper
    return decorator