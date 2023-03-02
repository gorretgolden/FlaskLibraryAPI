from backend.db import db
from dataclasses import dataclass


@dataclass
class Book(db.Model):
  __tablename__ = 'books'


  id: int
  title: str
  isbn: str
  publishing_date: str
  price: int
  price_unit:str
  user_id:int
  publishing_company_id:int
  created_at:str
  updated_at:str

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(100),unique=True)
  isbn = db.Column(db.String(50))  
  publishing_date = db.Column(db.String(200))
  price = db.Column(db.Integer)
  image = db.Column(db.String(255),nullable=True)
  price_unit = db.Column(db.String(10),default='UGX')
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  publishing_company_id = db.Column(db.Integer,db.ForeignKey('publishing_companies.id'))
  created_at = db.Column(db.String(255),nullable=True)
  updated_at = db.Column(db.String(255),nullable=True)


  def __init__(self, title, isbn,publishing_date,price,price_unit,image,user_id,publishing_company_id,created_at,updated_at):
   self.title = title
   self.isbn = isbn
   self.publishing_date = publishing_date
   self.price = price
   self.price_unit = price_unit
   self.image = image
   self.user_id = user_id
   self.publishing_company_id = publishing_company_id
   self.created_at = created_at
   self.updated_at = updated_at


  def __repr__(self):
        return f"<Book {self.title} >"
  

        
   #save a new instance
  def save(self):
        db.session.add(self)
        db.session.commit()

   #delete the item
  def delete(self):
        db.session.delete(self)
        db.session.commit()