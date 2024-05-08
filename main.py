from flask import Flask, render_template, url_for
from routes.user import user_route

app = Flask(__name__)

app.register_blueprint(user_route, url_prefix='/users')

app.run(debug=True)
