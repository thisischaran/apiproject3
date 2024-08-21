from flask.views import MethodView
from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from schema import opsrespschema, opsschema

blp = Blueprint("operations", __name__, description="operations")

@blp.route('/multiply')
class multiply(MethodView):
    @jwt_required()
    @blp.arguments(opsschema)
    @blp.response(201,opsrespschema)
    def post(self,user_data):

        numb1 = user_data["number1"]
        numb2 = user_data["number2"]

        result = float(numb1) * float(numb2)

        return {"result": result}