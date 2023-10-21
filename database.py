from sqlalchemy import LargeBinary,String
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class CatPicture(db.Model):
    id = db.Column(String(255), primary_key=True)
    picture_data = db.Column(LargeBinary, nullable=False)
        


