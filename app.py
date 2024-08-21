from flask import Flask
from flask_jwt_extended import JWTManager
from flask_smorest import Api
from resources.users import blp
from resources.operations import blp as opsblp
from db import db

app = Flask(__name__)
app.config["PROPOGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "My rest api project"
app.config["API_VERSION"] = "V1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["JWT_SECRET_KEY"] ="charan"
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///mysite.db"
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)
api.register_blueprint(blp)
api.register_blueprint(opsblp)
with app.app_context():
    db.create_all()
if __name__ =='__main__':
    app.run(debug= True)