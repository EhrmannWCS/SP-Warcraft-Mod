## IMPORTS

from paths import PLUGIN_PATH

from .heroes.undead import Undead

## CONFIGURATION

LOG_PRIORITY = 0
LOG_LOCATION = PLUGIN_PATH / 'warcraft' / 'debug.log'

DATABASE_TYPE = 1 # Types = 1 (SQLite), 2 (MySQL), 3 (UNKOWN)
SQLITE_LOCATION = PLUGIN_PATH / 'warcraft' / 'data' / 'players.sqlite'
MYSQL_ADDRESS = None
MYSQL_LOGIN = None
MYSQL_PASSWORD = None
MYSQL_DATABASE_NAME = None

WARCRAFT_DEFAULT_HERO = Undead

WARCRAFT_KILL_EXPERIENCE = 50