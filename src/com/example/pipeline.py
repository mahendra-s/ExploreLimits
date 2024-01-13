import json

from src.com.example.config import Config
from src.com.example.my_logging import logging
import requests


class Pipeline:
    def __init__(self):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}

    def check_alive(self):
        res = requests.get(url=self.config.es_url)
        logging.error(res.json())

    @staticmethod
    def set_processor(key: str, value: str):
        return {
            "set": {
                "field": key,
                "value": value,
                "if": {"id": "my-prod-tag-script"}
            }
        }

    def pipeline_processors(self, **set):
        return [self.set_processor(key=key, value=val) for key, val in set.items()]

    def create_pipe(self, name: str, set: dict):
        res = requests.put(
            url=f"{self.config.es_url}/_ingest/pipeline/{name}",
            headers=self.headers,
            data=json.dumps({
                "processors": self.pipeline_processors(**set),
                "description": "elastic boost"
            })
        )
        logging.error(res.json())


if __name__ == "__main__":
    service = Pipeline()
    service.create_pipe(name="mysetup", set={"field1": "value1"})
