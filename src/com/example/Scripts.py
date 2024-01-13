import json

from src.com.example.config import Config
from src.com.example.my_logging import logging
import requests


class Scripts:
    def __init__(self,name:str):
        self.config = Config()
        self.headers = {'Content-type': 'application/json'}
        self.name=name
    def check_if(self):
        res = requests.put(
            url=f"",
            data=json.dumps({
                "script": {
                    "lang": "painless",
                    "source": """
      Collection tags = ctx.tags;
      if(tags != null){
        for (String tag : tags) {
          if (tag.toLowerCase().contains('prod')) {
            return false;
          }
        }
      }
      return true;
    """
                }
            })
        )


PUT
_scripts / my - prod - tag - script

PUT
_ingest / pipeline / my - pipeline
{
    "processors": [
        {
            "drop": {
                "description": "Drop documents that don't contain 'prod' tag",

            }
        }
    ]
}
