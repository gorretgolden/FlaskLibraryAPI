from flask import Blueprint,request,jsonify
from backend.publishIng_companies.model import PublishingCompany
from backend.db import db
from backend.publishIng_companies.model import PublishingCompany
import datetime

publishing_companies = Blueprint('publishing_companies',__name__,url_prefix='/publishing_companies')



#get all companies
@publishing_companies.route("/")
def all_publishing_companies():
    companies = PublishingCompany.query.all()
    return jsonify({"success":True,"data":companies,"total":len(companies)}),200


#create a new company
@publishing_companies.route('/new',methods=['POST'])
def create_new_book():

    #getting data from the request
    name = request.json('name')
    user_id = request.json('user_id')
    contact = request.json('contact')
    address = request.json('address')

  
    #validations
    if not contact or not user_id or name or address:
        return jsonify({'error':"Please enter all fields"})
    
    if PublishingCompany.query.filter_by(name=name).first() is not None:
        return jsonify({'error': "Publishing Company name is already in use"}), 409 

    
    if PublishingCompany.query.filter_by(contact=contact).first() is not None:
        return jsonify({'error': "Phone number is already in use"}),409
       

    #creating a new instance of a publishing company
    new_company = PublishingCompany(name=name,contact=contact,address=address,user_id=user_id) 
      
    #inserting values
    db.session.add(new_company)
    db.session.commit()

    return jsonify({
        "success":True,
        "message":"Publishing Company created successfully",
        "data":new_company
    }),201



#get company by id

@publishing_companies.route('/company/<int:id>')
def get_book(id):
    company = PublishingCompany.query.get_or_404(id)

    return {"success": True, "data":company,"books":company.books}




#update a publishing company
@publishing_companies.route('/book/<id>', methods=['PUT'])
def update_book(id):
    company = PublishingCompany.query.get_or_404(id)

    data = request.get_json()

    #validations
    if not data['name']:
            return jsonify({"message":"Company name is required"})
        
    if not data['contact']:
            return jsonify({"message":"Company contact address is required"})
        
    if not data['address']:
            return jsonify({"message":"Company address is required"})
        
    if not data['user_id'] :
            return jsonify({"message":"Company owner  is required"})
    

    company.name = data['name']
    company.contact = data['contact']
    company.address = data['address']
    company.user_id = data['user_id']
    company.updated_at = datetime.utcnow()
    db.session.add(company)
    db.session.commit()
    return {"message": f"Company {company.name} updated successfully"}


  
#deleting a company by an id
@publishing_companies.route("/<int:id>", methods=['DELETE'])
def delete_publishing_company(id):
    company = PublishingCompany.query.filter_by(id=id).first()

    if not company:
        return jsonify({"message":"Publishing Company not found"})
    else:    
       db.session.delete(company)
       db.session.commit()
       return jsonify({"message":f"Company {company.name} successfully deleted."}),200      

        
  


