
from marshmallow import Schema, fields


class userschema(Schema):
    userid = fields.Str(required=True)
    password = fields.Str(required=True)

class usersregresp(Schema):
    msg = fields.Str(dump_only=True)

class userlogresponse(Schema):
    jwttoken = fields.Str(dump_only=True)


class opsschema(Schema):
    number1= fields.Float(required=True)
    number2= fields.Float(required=True)

class opsrespschema(Schema):
    result= fields.Float(dump_only=True)

    