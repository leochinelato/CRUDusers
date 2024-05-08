from routes.user import user_route
from database.database import db
from database.models.user import User

def configure_all(app):
    configure_routes(app)
    configure_db()

def configure_routes(app):
    app.register_blueprint(user_route, url_prefix='/users')
    
def configure_db():
    db.connect()
    db.create_tables([User])