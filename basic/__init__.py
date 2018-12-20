import connexion
from flask_cors import CORS
from flask_marshmallow import Marshmallow

ma = Marshmallow()


def init_api():
    app = connexion.App(__name__, specification_dir="./swagger/")
    app.add_api("swagger.yaml", arguments={"title": "files"})
    CORS(app.app)
    ma.init_app(app.app)
    return app
