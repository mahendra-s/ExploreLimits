import logging as _logging
import os

import dotenv

if os.path.exists('.env'):
    dotenv.load_dotenv(".env")
if os.path.exists('.env.local'):
    dotenv.load_dotenv(".env.local")


def log_level():
    _log_level = os.getenv('LOG_LEVEL', 'INFO')
    print(f"Setting Log Level {_log_level}")
    return _log_level


logging = _logging.getLogger('zoetic-bots')
logging.setLevel(_logging.INFO)
