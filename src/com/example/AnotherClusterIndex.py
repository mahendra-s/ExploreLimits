import json

from src.com.example.config import Config
from src.com.example.my_logging import logging
import requests


class AnotherClusterIndex:
    def __init__(self):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}

    def check_alive(self):
        res = requests.get(url=f"{self.config.es_scheme}://{self.config.es_host_another}:{self.config.es_port_another}")
        logging.error(res.json())

    def create_index(self,index:str):
        res=requests.put(
            url=f"{self.config.es_scheme}://{self.config.es_host_another}:{self.config.es_port_another}/{index}"
        )
        logging.error(res.json())

if __name__ == "__main__":
    service = AnotherClusterIndex()
    service.check_alive()
    service.create_index(index="my_index")
