from flask import Flask
from configuration import configure_all

app = Flask(__name__)
app.secret_key = '9dwmdwq w09 dsm ew d @J 2) SADnOAUWD 0 saiojd Q(*W)'

configure_all(app)

app.run(debug=True)
