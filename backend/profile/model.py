from backend.db import db

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(255),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
   


    def __init__(self, image, user_id):
     self.image = image
     self.user_id = user_id
    

    def __repr__(self):
        return f"<Profile {self.image} >"
