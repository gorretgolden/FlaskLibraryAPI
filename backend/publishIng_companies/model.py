from backend.db import db
from dataclasses import dataclass


class PublishingCompany(db.Model):
  __tablename__ = 'publishing_companies'
  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(100),unique=True)
  address = db.Column(db.String(255))  
  contact = db.Column(db.String(200),unique=True)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  created_at = db.Column(db.String(255),nullable=True)
  updated_at = db.Column(db.String(255),nullable=True)
  books = db.relationship("Book",backref="publishing_company")


  def __init__(self, name,contact,address,user_id,created_at,updated_at):
   self.name = name
   self.contact = contact
   self.address = address
   self.user_id = user_id
   self.created_at = created_at
   self.updated_at =updated_at

  

  def __repr__(self):
        return f"<PublishingCompany {self.name} >"
  

        
