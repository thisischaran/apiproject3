
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from schema import userschema,userlogresponse,usersregresp
from db import db
from models.users import userstab
from flask_jwt_extended import create_access_token
from passlib.hash import pbkdf2_sha256

from sqlalchemy.exc import SQLAlchemyError, IntegrityError



blp = Blueprint("users",__name__, description="useroperation")


@blp.route('/register')
class userregister(MethodView):
    @blp.arguments(userschema)
    @blp.response(201,usersregresp)
    def post(self,user_data):

        item = userstab(**user_data)
        gh = pbkdf2_sha256.hash(item.password)
        item.password =gh

        try:
            db.session.add(item)
            db.session.commit()
            return {"msg": "usercreated sucessfully"}
        except IntegrityError:
            abort(400, message= "id already exisit")
        except SQLAlchemyError:
            abort(400, message= "somethiong wrong")


@blp.route('/login')
class userrlogin(MethodView):
    @blp.arguments(userschema)
    @blp.response(201,userlogresponse)
    def post(self,user_data):
        item = userstab(**user_data)
        userexi = userstab.query.filter_by(userid= item.userid).first()
        if userexi:
           print(pbkdf2_sha256.verify(item.password,userexi.password))
           if  pbkdf2_sha256.verify(item.password,userexi.password):
               jwttoken = create_access_token(identity=item.userid)
               return {"jwttoken":jwttoken}
           abort(400,message="invalid pasword")
        abort(400,message="userid not found")

        

