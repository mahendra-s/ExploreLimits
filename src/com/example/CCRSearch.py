import json

from src.com.example.config import Config
from src.com.example.my_logging import logging
import requests


class CCRSearch:
    def __init__(self):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}

    def check_alive(self):
        res = requests.get(url=f"{self.config.es_scheme}://{self.config.es_host_another}:{self.config.es_port_another}")
        logging.error(res.json())

    def check_remote(self):
        res = requests.get(url=f"{self.config.es_url}/_remote/info")
        logging.error(res.json())

    def add_cluster(self):
        res = requests.put(
            url=f"{self.config.es_url}/_cluster/settings",
            headers=self.headers,
            data=json.dumps({
                "persistent": {
                    "search": {
                        "remote": {
                            "cluster_one": {
                                "seeds": [
                                    f"{self.config.es_host_another}:{self.config.es_port_transport_another}"
                                ]
                            }
                        }
                    }
                }
            })
        )
        logging.error(res.json())

    def ccr_search(self, index_name: str, cluster_name='cluster_one'):
        # GET /cluster_one:twitter/_search
        res = requests.get(
            url=f"{self.config.es_url}/{cluster_name}:{index_name}/_search",
        )
        logging.error(res.json())


if __name__ == "__main__":
    service = CCRSearch()
    service.check_alive()
    service.check_remote()
    service.add_cluster()
    service.check_remote()
    service.ccr_search(index_name="my_index")
