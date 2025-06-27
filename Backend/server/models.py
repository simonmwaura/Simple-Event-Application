from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(100),unique=True,nullable= False)
    password = db.Column(db.String(100),nullable=False)
    phone_number = db.Column(db.String(13),nullable=False)
    is_admin = db.Column(db.Boolean,default=False,nullable=False)
    is_organizer = db.Column(db.Boolean,default=False,nullable=False),
    
    events = db.relationship('Event',backref='organizer',lazy=True)
    registrations =db.relationship('Registration',backref='user',lazy=True)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer,primary_key=True)
    event_name = db.Column(db.String(100), nullable = False)
    description = db.Column(db.Text, nullable=False)
    event_date = db.Column(db.DateTime,nullable=False)
    location = db.Column(db.String(100),nullable=False)
    organizer_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable= False)

    registrations = db.relationship('Registration',backref='event',lazy=True)

class Registration(db.Model):
    __tablename__ = 'registrations'
    registration_id = db.Column(db.Integer,primary_key = True)
    event_id = db.Column(db.Integer,db.ForeignKey('events.id'),nullable= False)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    registration_date = db.Column(db.DateTime,default = datetime.utcnow)

