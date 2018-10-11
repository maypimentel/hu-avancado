from flask import Blueprint, Flask, url_for

core_bp = Blueprint('core', __name__)


@core_bp.route('/')
def hello_world():
    return "Hello world"


def init_app(app: Flask, url_prefix='/'):
    app.register_blueprint(core_bp, url_prefix=url_prefix)
