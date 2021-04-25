import logging
import os
from starlette.applications import Starlette
from starlette.routing import Route, Mount
import uvicorn

from config import Config
from constants import LOG_DIR, CONFIG_FILE_PATH
from storage.postgres import PostgresStorage
from handlers.user_handler import UserHandler

# Config init
config = Config(yaml_file=CONFIG_FILE_PATH)

# Logger init
logger = logging.getLogger("main")
logger.setLevel(logging.DEBUG)

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Set log handler
fh = logging.FileHandler(f"{LOG_DIR}/all.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
logger.addHandler(fh)

# Init database
storage = PostgresStorage(
    host=config.DBHOST,
    port=config.DBPORT,
    dbname=config.DBNAME,
    username=config.DBUSER,
    password=config.DBPASSWORD
)

# Event on app startup
async def startup():
    await storage.connect()

# Routes
routes = [
    Mount('/users', routes=[
        Route('/', endpoint=UserHandler),
    ])
]

# Init app
app = Starlette(debug=config.DEBUG, routes=routes, on_startup=[startup])

if __name__ == '__main__':
    uvicorn.run(app=app, host=config.HOST, port=config.PORT)