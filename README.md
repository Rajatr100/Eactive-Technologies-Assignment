# Eactive-Technologies-Assignment
<br>
author-Rajat Raj


Features

/hello → Returns "Hello World!"

/users → Displays all users in a table

/new_user → Add a new user via HTML form

/users/<id> → View a specific user’s details

Error handling for missing users (404 page)

⚙️ Environment Setup
1️- Install Python

Make sure Python 3.x is installed.
Check your version:

python --version

2️- Install Dependencies

Install Flask (and optionally virtualenv for isolation):

pip install flask


(No MySQL needed — we r using SQLite.)

3️- Project Structure
flask_project/
│
├── app.py
├── init_db.py
├── schema.sql
├── users.db
│
└── templates/
    ├── users.html
    ├── new_user.html
    └── user_detail.html

4- Database Setup
Database Name:

users.db (SQLite)

Table Name:

users

Column	Type	Constraints
id	INTEGER	Primary Key, Auto Increment
name	TEXT	Not Null
email	TEXT	Unique, Not Null
role	TEXT	Not Null
 Schema File — schema.sql
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
);

INSERT INTO users (name, email, role) VALUES
('Rajat', 'rajat@example.com', 'Admin'),
('Neha', 'neha@example.com', 'Editor'),
('Amit', 'amit@example.com', 'Viewer');

 Initialize the Database

Run this once to create the database and populate sample data:

python init_db.py




Then open your browser and go to:

Route	URL	Description
/	http://127.0.0.1:5000/
	Home page
/hello	http://127.0.0.1:5000/hello
	Hello World
/users	http://127.0.0.1:5000/users
	All users
/new_user	http://127.0.0.1:5000/new_user
	Add new user
/users/<id>	e.g. http://127.0.0.1:5000/users/1
	View user details


