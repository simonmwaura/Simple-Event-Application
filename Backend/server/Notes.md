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


## Seed.py