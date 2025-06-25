from faker import Faker
from models import db,User,Event,Registration
from app import app
from datetime import datetime

faker = Faker()

print("<------Start Seeding------->")
def seed_data():
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        password = 'securepassword123'

        users = [
            User(name='Admin User',email='admin@example.com',password=password ,phone_number='+254712321478',is_admin=True,is_organizer=False),
            User(name="Organizer One",email='organizer1@example.com',password=password,phone_number='+254712321345',is_admin=False,is_organizer=True),
            User(name="Organizer Two",email='organizer2@example.com',password=password,phone_number='+254712321000',is_admin=False,is_organizer=True),
            User(name="User One",email='user1@example.com',password=password,phone_number='+254712321105',is_admin=False,is_organizer=False),
            User(name="User Two",email ='user2@example.com',password=password,phone_number='+254745907366',is_admin=False,is_organizer=False),
            User(name="User Three",email='user3@example.com',password=password,phone_number='+254739780900',is_admin=False,is_organizer=False)
        ]
        for user in users:
            db.session.add(user)
        db.session.commit()

        events = [
            Event(event_name="Tech Conference 2024",description='A conference about the latest in tech.',event_date = datetime(2024, 9, 1, 9, 0),location="Lavington,Nairobi",organizer_id=users[1].id),
             Event(event_name="Music Festival",description='A fun music festival with various artists',event_date = datetime(2024,10,15,9,0),location="Kilimani,Nairobi",organizer_id=users[2].id)
        ]

        for event in events:
            db.session.add(event)
        db.session.commit()

        registrations=[
            Registration(event_id=events[0].id , user_id = users[3].id),
            Registration(event_id=events[0].id , user_id = users[4].id),
            Registration(event_id=events[1].id , user_id = users[5].id)
        ]
        for registration in registrations:
            db.session.add(registration)
        
        db.session.commit()

seed_data()
print('<-----Seeding Completed---->')

