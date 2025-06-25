from flask import Flask
from flask_migrate import Migrate
from models import db,User,Event,Registration

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///EventsDatabase.db"

migrate = Migrate(app,db)
db.init_app(app)

@app.route('/')
def hello():
    return "Hello, World!"
