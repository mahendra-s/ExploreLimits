import json

from src.com.example.config import Config
from src.com.example.pipeline import Pipeline
from src.com.example.my_logging import logging
import requests


class UpdateStatus:
    def __init__(self, index, set_processors: dict = {"status": "Successful"}):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}
        self.pipe_name = f"update_{index}"
        Pipeline().create_pipe(name=self.pipe_name, set=set_processors)
        self.idx = index
        self.action = f'/{self.idx}/_update_by_query?pipeline="{self.pipe_name}"&wait_for_completion=false'

    def schedule(self, cron: str = "0 0/33 * * * ?"):
        # <seconds> <minutes> <hours> <day_of_month> <month> <day_of_week> [year]
        res = requests.put(
            url=f"{self.config.es_url}/_xpack/watcher/watch/my-watch",
            headers=self.headers,
            data=json.dumps(
                {
                    "trigger": {
                        "schedule": {"cron": cron}
                    },
                    "input": {
                        "http": {
                            "request": {
                                "scheme": self.config.es_scheme,
                                "host": self.config.es_host,
                                "port": int(self.config.es_port),
                                "path": self.action,
                                "method": "get",
                                "body": ""
                            }
                        }
                    }})
        )
        logging.error(res.json())


if __name__ == "__main__":
    service = UpdateStatus(index="index_here", set_processors={"status": "Successful"})
    service.schedule()
