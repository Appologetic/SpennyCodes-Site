# ----- Standard Library ------

# ----- External Dependencies -----
from flask import Blueprint, render_template

# ----- Internal Dependencies -----


###############################################################################
# ----- Define the Main Blueprint To Register it in __init__.py -----
main_blueprint = Blueprint("main", __name__)

# ----- Main Application Routes -----


@main_blueprint.route("/")
def index():
    return render_template("index.jinja")
