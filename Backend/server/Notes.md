## Models.py

USERS MODEL
- An organizer can create/update/view an event and the users attending that event.
- An admin can view all the events and users BUT cannot add or update an event.
- This is why the is_admin and is_organizer fields are important.

When trying to fetch an event ensure that the person who is fetching an event is an organizer and the event that they are fetching belongs to them.

EVENT MODEL
- A user has many events and it therefore has many registrations .
- An event belongs to an organizer.

REGISTRATION MODEL
- A user can register to multiple events and multiple registration.
-ONLY a normal user can register not an admin/organizer.


## Authentication and Authorization
Authentication(login)- A process of identifying who the user is. 
Authorization - After authentication is complete it is the process of allowing a user to access certain features . 

### Types of Authentication
1. Basic Authentication - Cookies
2. JWT Authentication - Tokens 

#### Steps
1. Any password passed by the user should actually be encrypted before being saved by the database using the following python packages bycrypt.
- command: pipenv install Flask-Bcrypt
- This is important as it makes our password not readable.

2. In the app.py file import bycrypt
- from flask_bcrypt import Bcrypt

3. Initialize it in the app.py
- bcrypt = Bcrypt()

4. Note this is not one of the steps 
1. Add a user
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

    The difference between name =data['name'], and  phone_number = data.get('phone_number')  is that the first one gives direct access meaning it is a must whereas in the second one it is not a must meaning if there is no phone number it is okay . 

5.  use of bcrypt.generate_password_hash in the password field
- For example :
- original - password = data['password'],
- result -   password = bcrypt.generate_password_hash(data['password']),

6. the result is this it is not correct because we want our password to be hashed.

- original password - 12345678
- stored   password - $2b$12$bO7TrgeJvCuOCCf7PtGSTuLMMIVMbKdUpUk/W.6Ynk64ALDGmVX7m

-original statement - password = bcrypt.generate_password_hash(data['password']),
-correct statement - password = bcrypt.generate_password_hash(data['password']).decode('utf-8'),

final password looks like $2b$12$quFIDVX8NgU2zhXXGiUD5OJ6AnYqrm8RSXKjHf2B6xUEzWn9H6dOe

that was about hashing not jwt authentication.

7. Begining JWT authentication by installing the correct package.
- command = pipenv install Flask-JWT-Extended

8. import the packages from the documentation.
- starting with 
import 1 - from flask_jwt_extended import JWTManager
 -this is because JWTManager is used to manage and configure the functionality of jwt in your application.

9. initialize your jwt to our application and it configurers all out routes
jwt = JWTManager(app)

10. configure the JWT secret key :  app.config["JWT_SECRET_KEY"] = "super-secret"
- This is very important because it is used to sign and verify any jwt token .
- ensure you can pass some random values where the "super-secret" is and randomized values.
- use a randomized value.
a. import random
b. app.config["JWT_SECRET_KEY"] = "eqesdvsdgddfggfdgg" + str(random.randint(1,1000000))