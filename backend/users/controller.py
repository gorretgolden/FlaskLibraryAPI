#register a new user
from flask import  jsonify, request, Blueprint
from werkzeug.security import check_password_hash,generate_password_hash
from backend.users.model import User
from backend.db import db
import datetime

users = Blueprint('users', __name__, url_prefix='/users')

#get all users
@users.route("/")
def all_users():
    users= User.query.all()
    return jsonify({
            "success":True,
            "data":users,
            "total":len(users)
        }),200


@users.route('/create', methods= ['POST',"GET"])
def create_user():
    data = request.get_json()
    
    if request.method == "POST":
          
      name = data['name']
      email = data['email']
      contact = data['contact']
      user_type = data['user_type']
      password = data['password']


  
      #validations
      if not contact:
              return jsonify({'error':"Please enter all fields"})
      
      if not name:
              return jsonify({'error':"First name is required"})
      

      if len(password) < 6:
            return jsonify({'error': "Password is too short"}), 400



      if User.query.filter_by(email=email).first() is not None:
        return jsonify({'error': "Email is already in use"}), 409 

    
      if User.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': "Phone number is already in use"}),409
       

      #creating a hashed password in the database
      hashed_password = generate_password_hash(password,method="sha256")
      new_user = User(name=name,email=email,contact=contact,user_type=user_type,password=hashed_password,created_at=datetime.now()) 
      
      #inserting values
      db.session.add(new_user)
      db.session.commit()
      return jsonify({'message':'New user created sucessfully','data':new_user}),200
          
   
    elif request.method == "GET":
        users= User.query.all()
        return jsonify({
            "success":True,
            "data":users,
            "total":len(users)
        })
        
      



#get author books
@users.route("/author/<int:id>/books")
def get_all_author_books(id):
    user = User.query.filter_by(id=id).first()
    books  = user.books
    return jsonify({
            "success":True,
            "data":books,
            "total":len(users)
        }),200



@users.route('/user/<user_id>', methods=['GET', 'PUT', 'DELETE'])
def handle_user(user_id):
    user = User.query.get_or_404(user_id)

    if request.method == 'GET':
        response = {
            "id":user.id,
            "name": user.name,
            "user_type":user.user_type,
            "email": user.email,
            "contact": user.contact
        }
        return {"success": True, "user": response,"message":"User details retrieved"}

    elif request.method == 'PUT':
        data = request.get_json()

        if not data['name']:
            return jsonify({"message":"Your name is required"})
        
        if not data['email']:
            return jsonify({"message":"Your email address is required"})
        
        if not data['contact']:
            return jsonify({"message":"Your contact is required"})
        
        if not data['password'] or len(data['password'])<6:
            return jsonify({"message":"Your password is required and must be greater than 6 characters"})
        
        user.name = data['name']
        user.email = data['email']
        user.contact = data['contact']
        user.password = generate_password_hash(data['password'])
        user.updated_at = datetime.utcnow()
        db.session.add(user)
        db.session.commit()
        return {"message": f"User details of {user.name} updated successfully"}

    elif request.method == 'DELETE':
        db.session.delete(user)
        db.session.commit()
        return {"message": f"User {user.name} successfully deleted."}   
  
        
  
   
#get user books
@users.route('/user/<user_id>/books', methods=['GET'])
def user_books(user_id):
    user = User.query.get_or_404(user_id)
    books = user.books
    return jsonify({'message':'User  book'})



