from flask import Flask,request,jsonify
from flask_migrate import Migrate
from models import db,User,Event,Registration
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///EventsDatabase.db"

migrate = Migrate(app,db)
db.init_app(app)

# 1. Add a user
@app.route('/users',methods = ['POST'])
def create_user():
    data = request.get_json()
    new_user = User(
        name =data['name'],
        email = data['email'],
        password = data['password'],
        phone_number = data.get('phone_number'),
        is_admin = data.get('is_admin',False),
        is_organizer = data.get('is_organizer',False)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message":"User created succcessfully"}),201

# 2. Fetch all users 
@app.route('/users',methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({"id":user.id,"name":user.name, "email":user.email, "password":user.password, "phone_number":user.phone_number,"is_admin":user.is_admin,"is_organizer":user.is_organizer})
    return jsonify(user_list),200

# 3. Update user
@app.route('/users/<int:id>',methods=["PUT"])
def update_user(id):
    data = request.get_json()
    user = User.query.get(id)
    if user is None:
        return jsonify({"Message":"User not found."}),404
    
    user.name = data.get('name',user.name)
    user.email = data.get('email',user.email)
    user.password = data.get('password',user.password)
    user.phone_number = data.get('phone_number',user.phone_number)
    user.is_admin = data.get('is_admin',user.is_admin)
    user.is_organizer = data.get('is_organizer',user.is_organizer)
    db.session.commit()
    return jsonify({"message":"User updated successfully"}),200

# 4. Delete user
@app.route('/users/<int:id>',methods=["DELETE"])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"message":"User not found"}),404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message":"User deleted successfully"}),404

# 5. Add an event
@app.route('/events',methods=["POST"])
def create_event():
    data = request.get_json()
    new_event = Event(
        event_name = data['event_name'],
        description = data['description'],
        event_date = datetime.strptime(data['event_date'],'%Y-%m-%d %H:%M:%S'),
        location = data['location'],
        organizer_id = data['organizer_id']
    )
    db.session.add(new_event)
    db.session.commit()
    return jsonify({"message":"Event created successfully"}),201

# 6. Fetch all events
@app.route('/events',methods=["GET"])
def get_events():
    events = Event.query.all()
    events_list = []
    for event in events:
        events_list.append({"id":event.id,"event_name":event.event_name,"description":event.description,"event_date":event.event_date.strftime('%Y-%m-%d %H:%M:%S'),"location":event.location,"organizer_id":event.organizer_id})
    return jsonify(events_list),200

#7. Delete all events
@app.route('/events/<int:id>',methods=["DELETE"])
def delete_events(id):
    event = Event.query.get(id)
    if event is None:
        return jsonify({"message":"Event not found"}),404
    db.session.delete(event)
    db.session.commit()
    return jsonify({"message":"Event deleted successfully"}),404

#8. Update an event
@app.route('/events/<int:id>',methods=["PUT"])
def update_events(id):
    data = request.get_json()
    event = User.query.get(id)
    if event is None:
        return jsonify({"Message":"Event not found."}),404
    
    event.event_name = data.get('event_name',event.event_name)
    event.description = data.get('description',event.description)
    event.event_date = datetime.strptime(data.get('event_date',event.event_date.strftime('%Y-%m-%d %H:%M:%S')))
    event.location = data.get('location',event.location)
    event.organizer_id = data.get('organizer_id',event.organizer_id)
    db.session.commit()
    return jsonify({"message":"Event updated successfully"}),200

#9. Fetch events by id
@app.route('/events/<int:id>',methods=["GET"])
def get_single_event(id):
    event = Event.query.get(id)
    if event is None:
        return jsonify({"message":"Event not found"}),404
    return jsonify({
        "id":event.id,
        "event_name":event.event_name,
        "description":event.description,
        "event_date":event.event_date.strftime('%Y-%m-%d %H:%M:%S'),
        "location":event.location,
        "organizer_id":event.organizer_id
    }),200

#10. Add a registration
@app.route('/registrations',methods=['POST'])
def create_registation():
    data = request.get_json()
    new_registration= Registration(
        event_id = data['event_id'],
        user_id = data['user_id'],
        registration_date = datetime.strptime(data['registration_date'],'%Y-%m-%d %H:%M:%S')
    )
    db.session.add(new_registration)
    db.session.commit()
    return jsonify({"message":"Registration created successfully"}),201

#11. Fetch all registrations
@app.route('/registrations',methods=["GET"])
def get_registration():
    registrations = Registration.query.all()
    registration_list = []
    
    for registration in registrations:
        registration_list.append( {"id":registration.id,"event_id":registration.event_id, "user_id":registration.user_id,"registration_date":registration.registration_date.strftime('%Y-%m-%d %H:%M:%S')})
    return jsonify(registration_list),200

#12. Fetch single registration
@app.route('/registrations/<int:id>',methods=["GET"])
def get_single_registration(id):
    registration = Registration.query.get(id)
    if registration is None:
        return jsonify({"message":"Registration not found"}),404
    return jsonify({
        "id":registration.id,
        "event_id":registration.event_id,
        "user_id":registration.user_id,
        "registration_date":registration.registration_date.strftime('%Y-%m-%d %H:%M:%S')
    }) , 200

#13.Update registration
@app.route('/registrations/<int:id>',methods=["PUT"])
def update_registration(id):
    data = request.get.json()
    registration= Registration.query.get(id)
    if registration is None:
        return jsonify({"Message":"Registration not found"}),404
    registration.event_id = data.get("event_id",registration.event_id)
    registration.user_id = data.get("user_id",registration.user_id)
    registration.registration_date = datetime.strptime(data.get('registration_date',registration.registration_date.strftime('%Y-%m-%d %H:%M:%S')))
    db.session.commit()
    return jsonify({"message":"Registration deleted successfully"}),200   

#14. Delete registration
@app.route('/registrations/<int:id>' , methods = ['DELETE'])
def delete_regisitration(id):
    registration = Registration.query.get(id)
    if registration is None:
        return jsonify({"message":"Registration not found"}),404
    db.session.delete(registration)
    db.session.commit()
    return jsonify({"message":"Registration deleted successfully"}),200

if __name__ == '__main__':
    app.run(debug=True)