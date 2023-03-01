from flask import Blueprint,jsonify,request
from backend.books.model import Book
from backend.db import db
from datetime import datetime

books = Blueprint('books',__name__,url_prefix='/books')





#get all books
@books.route("/")
def all_books():
    books= Book.query.all()
    return jsonify({"success":True,"data":books,"total":len(books)}),200


#create a new book
@books.route('/new', methods= ['POST'])
def create_new_book():

    title =  request.json('title')
    isbn = request.json('isbn')
    price = request.json('price')
    publishing_date = request.json('publishing_date')
    image = request.json('image')
    user_id = request.json('user_id')
    publishing_company_id = request.json('publishing_company_id')
    created_at = datetime.now()
      
  
    #validations
    if not title or not isbn or not price or not publishing_date or not user_id or not publishing_company_id:
        return jsonify({'error':"Please enter all fields"})
      

    if Book.query.filter_by(title=title).first() is not None:
        return jsonify({'error': "A book with this name already exists"}), 409 


    #inserting values
    new_book = Book(title=title,isbn=isbn,price=price,image=image,publishing_date=publishing_date,user_id=user_id,publishing_company_id=publishing_company_id,created_at=created_at)
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message':'New book created sucessfully','data':new_book}),201
          
   
    
        

#get book by id

@books.route('/book/<int:id>')
def get_book(id):
    book = Book.query.get_or_404(id)

    return {"success": True, "data":book,"author":book.user}


#update a book
@books.route('/book/<id>', methods=['PUT'])
def update_book(id):
    book = Book.query.get_or_404(id)


    data = request.get_json()

    if not data['title']:
            return jsonify({"message":"Your title is required"})
        
    if not data['isbn']:
            return jsonify({"message":"Your isbn address is required"})
        
    if not data['price']:
            return jsonify({"message":"Your price is required"})
        
    if not data['publish_date'] :
            return jsonify({"message":"Book publish date is required"})
    
    if not data['user_id'] :
            return jsonify({"message":"Book author is required"})
    
    if not data['publishing_company_id'] :
            return jsonify({"message":"Book publishing company is required"})
        

    book.title = data['title']
    book.price = data['price']
    book.isbn = data['isbn']
    book.publish_date = data['publish_date']
    book.user_id = data['user_id']
    book.publishing_company_id = data['publishing_company_id']
    book.updated = datetime.now()
    db.session.add(book)
    db.session.commit()
    return {"message": f"Book {book.title} updated successfully"}


  
#deleting a book by an id
@books.route("/<int:id>", methods=['DELETE'])
def delete_books(id):
    book = Book.query.filter_by(id=id).first()

    if not book:
        return jsonify({"message":"Book not found"})
    else:    
       db.session.delete(book)
       db.session.commit()
       return jsonify({"message":f"Book {book.name} successfully deleted."}),200      

        
  


