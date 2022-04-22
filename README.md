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

### /register [POST]


```json
{
    "firstname": "Anakin",
    "lastname": "Skywalker",
    "email": "anakin@skywalker.space",
    "password": "padme_amidala"
}
```

**Response**

* 200: Success

* 400: Bad request

* 409: Email already exists

### /login [POST]


```json
{
    "email": "anakin@skywalker.space",
    "password": "padme_amidala"
}
```

**Response**

* 200: Success

* 400: Bad request

* 401: Email or password incorrect

### /logout [GET]

Actually, logout endpoint does nothing. It sends only 200 response without Authorization header whether user logged in or not. 

### /posts/create [POST]

```json
{
    "title": "anakin@skywalker.space",
    "text": "padme_amidala",
    "is_deleted": false,
    "is_draft": false
}
```

**Response**

* 200: Post created

* 400: Bad request

* 401: Login required

### /posts/list{?page=1} [GET]

**Response**

* 200: Success

### /posts/<int:year>/<int:month>/<int:day>/<string:title> [GET]

**Response**

* 200: Success
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
