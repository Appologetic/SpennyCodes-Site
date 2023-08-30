# ----- Standard Library ------

# ----- External Dependencies -----
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import force_auto_coercion
from flask_assets import Environment, Bundle

# ----- Internal Dependencies -----
from app.config import set_config


###############################################################################
# ----- Initialize and Configure the Flask App -----

app = Flask(__name__, static_folder="static")
set_config(app)


# ----- Set up connection to the DB -----

db = SQLAlchemy(app)
force_auto_coercion()


# ----- Register Blueprints -----

from app.main import main_blueprint

app.register_blueprint(main_blueprint)


# ----- Bundle JS and CSS Assets for delivery -----
assets = Environment(app)

# bundle js
js = Bundle("js/bootstrap.bundle.js", "js/htmx.min.js", output="bundled/packed.js")
assets.register("js_all", js)

# bundle css
css = Bundle("css/bootstrap.css", "css/fonts.css", output="bundled/packed.css")
assets.register("css_all", css)
