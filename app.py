from backend import create_app, db
from flask_migrate import Migrate
from backend.users.model import User
from backend.profile.model import Profile
from backend.publishIng_companies.model import PublishingCompany
from backend.books.model import Book


app = create_app('development')
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   return dict(db=db, User=User)