# Orion

Orion is a headless blog API system

## Installation

Clone the repository
```bash
git clone https://github.com/ahmetelgun/Orion.git
cd Orion
```

Activate virtualenv and install requirements
```bash
pipenv shell
pip install -r requirements.txt
```

Run tests
```bash
python -m unittest
```

Create Database
```bash
python models.py
```

Start the application
```bash
python app.py
```

## Usage

Orion has 4 enpoints.

### /register [POST]

#### Body

```json
{
    "firstname": "Anakin",
    "lastname": "Skywalker",
    "email": "anakin@skywalker.space",
    "password": "padme_amidala"
}
```

#### Response

Response takes 3 different response codes.

If user successfully created, returns 200.

If request is invalid, returns 400.

If email is already exists, returns 409.

*Response with 200 status code*
```json
{
    "message": "User successfuly created"
}
```

### /login [POST]

#### Body

```json
{
    "email": "anakin@skywalker.space",
    "password": "padme_amidala"
}
```

#### Response

Response takes 3 different response codes.

If loggin success, returns 200 with JWT Token in Authorization header.

If request is invalid, returns 400.

If email or password incorrect, returns 401.

*Response with 200 status code*
```json
{
    "message": "Login success"
}
```

### /logout [GET]

Actually, logout endpoint does nothing. It sends only 200 response without Authorization header whether user logged in or not. 

### / [GET]

/ endpoint is the test endpoint for authentication. If you send a valid JWT Token in Authorization header, you get a response with 200 status code like this:

```json
{
    "message": "welcome, Anakin"
}
```

If you send a invalid JWT Token in Authorization header, you get a response with 401 status code like this

```json
{
    "message": "Login required"
}
```
