import json

from src.com.example.config import Config
from src.com.example.my_logging import logging
import requests


class Service1:
    def __init__(self):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}

    def check_alive(self):
        res = requests.get(url=self.config.es_url)
        logging.error(res.json())

    def check_lisense(self):
        res = requests.get(url=f"{self.config.es_url}/_xpack/license/trial_status")
        logging.error(res.json())

    def start_lisense(self):
        res = requests.post(url=f"{self.config.es_url}/_xpack/license/start_trial?acknowledge=true")
        logging.error(res.json())

    def start_basic(self):
        res = requests.post(url=f"{self.config.es_url}/_xpack/license/start_basic?acknowledge=true")
        logging.error(res.json())

    def pipeline_processors(self):
        return [
            {
                "set": {
                    "field": "field",
                    "value": "value"
                }
            }
        ]

    def create_pipe(self, name: str):
        res = requests.put(
            url=f"{self.config.es_url}/_ingest/pipeline/{name}",
            headers=self.headers,
            data=json.dumps({
                "processors": self.pipeline_processors(),
                "description": "elastic boost"
            })
        )
        logging.error(res.json())

    def update_setting(self, settings: dict = {
        "index": {
            "refresh_interval": "1h",
            # "default_pipeline": "default-pipeline"
        }
    }):
        res = requests.put(
            url=f"{self.config.es_url}/_all/_settings?preserve_existing=true",
            headers=self.headers,
            data=json.dumps(settings)
        )
        logging.error(res.json())


if __name__ == "__main__":
    service = Service1()
    service.check_alive()
    # service.check_lisense()
    # service.start_lisense()
    # service.start_basic()
    service.update_setting()
