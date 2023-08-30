# ----- Standard Library ------
import os

# ----- External Dependencies -----
from dotenv import load_dotenv, find_dotenv

# ----- Internal Dependencies -----


###############################################################################
# ----- Locate and Load the .flaskenv file -----

load_dotenv(find_dotenv(".flaskenv"))

# ----- Setting File Directory for Paths -----

directory = os.path.abspath(os.path.dirname(__file__))

# ----- Configuration Classes -----


class ProdConfig:
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        directory, "data", "dev_insertdbname.sqlitedb"
    )


class DevConfig(ProdConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        directory, "data", "prod_insertdbname.sqlitedb"
    )


# ----- Setting the Config Based on .flaskenv -----


def set_config(app):
    env = os.getenv("ENVIRONMENT").lower()
    if env == "development":
        app.config.from_object(DevConfig)
    elif env == "production":
        app.config.from_object(ProdConfig)
