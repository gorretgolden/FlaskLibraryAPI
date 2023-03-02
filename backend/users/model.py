from backend.db import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
  __tablename__ = 'users'

  id: int
  name: str
  email: str
  contact: str
  user_type: str

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100),nullable=False)
  email = db.Column(db.String(50))  
  contact = db.Column(db.String(200))
  user_type = db.Column(db.String(100),default="author")
  password = db.Column(db.String(10))
  created_at = db.Column(db.String(255),nullable=True)
  updated_at = db.Column(db.String(255),nullable=True)
  profile = db.relationship("Profile", uselist=False, backref="user")
  books = db.relationship("Book",backref="user")
  


  def __init__(self, name, email,contact,user_type,password,created_at,updated_at):
   self.name = name
   self.email = email
   self.contact = contact
   self.user_type = user_type
   self.password = password
   self.created_at = created_at
   self.updated_at =updated_at

  


  def __repr__(self):
        return f"<User {self.name} >"
  

        
   #save a new instance
  def save(self):
        db.session.add(self)
        db.session.commit()

   #delete the item
  def delete(self):
        db.session.delete(self)
        db.session.commit()
 