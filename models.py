from extensions import db
from app import app
# from datetime import datetime

class Blogs(db.Model):

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(30),nullable=True)
    description = db.Column(db.String(255),nullable=True)

    # created_at = db.Column(db.DateTime(),nullable=True,default=datetime.utcnow)
    # updated_at = db.Column(db.DateTime(),nullable=True,default=datetime.utcnow)

    def __repr__(self):
        return self.title
    def __init__(self,title):
        self.title=title