from flask import Blueprint

auth = Blueprint('auth',__name__,url_prefix='/auth')


#user registration
@auth.route('/register')
def create_user():
    pass