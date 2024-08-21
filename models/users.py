from db import db

class userstab(db.Model):
    __tablename__ ="users"

    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(50), nullable = False, unique =True)
    password = db.Column(db.String(300), nullable = False)