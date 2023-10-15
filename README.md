
# Rest API Contacts

This project is a RESTful API for managing contacts. It also features a JWT-based authentication and authorization system.

## Main Features:

- User registration.
- User authentication with JWT generation.
- Adding, editing, deleting, and viewing contacts.
- Each user can only access their own contacts.

## Installation and Running:

1. Install the necessary dependencies:
```
pip install -r requirements.txt
```

2. Start the server:
```
uvicorn main:app --reload
```

## Using the API:

### User Registration:

POST `api/auth/signup`

Parameters: 
- `username`: User's name
- `email`: User's email address
- `password`: User's password

### Authentication:

POST `api/auth/login`

Parameters:
- `email`: User's email address
- `password`: User's password

### Managing Contacts:

- GET `/api/contacts/all`: Retrieve a list of all contacts for the user.
- POST `/api/contacts`: Add a new contact.
- GET `/api/contacts/{contact_id}`: Get details of a specific contact.
- PUT `/api/contacts/{contact_id}`: Update a contact.
- DELETE `/api/contacts/{contact_id}`: Delete a contact.
- GET `/api/contacts/find/{query}`: Search contacts by email or name.
- GET `api/contacts/birthday/{days}`: Upcomming birthdays for the next 7 days.
