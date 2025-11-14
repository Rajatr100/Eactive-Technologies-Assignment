from flask import Flask, render_template, request, redirect, url_for, abort, flash
import sqlite3
import os




app = Flask(__name__)
app.secret_key = "dev-secret" 

DB_NAME = "users.db"

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    return conn

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/users")
def list_users():
    conn = get_db_connection()
    users = conn.execute("SELECT * FROM users").fetchall()
    conn.close()
    return render_template("users.html", users=users)

@app.route("/new_user", methods=["GET", "POST"])
def new_user():
    if request.method == "POST":
        name = request.form["name"].strip()
        email = request.form["email"].strip()
        role = request.form["role"].strip()

        if not name or not email or not role:
            flash("All fields are required!", "error")
            return render_template("new_user.html")

        try:
            conn = get_db_connection()
            conn.execute(
                "INSERT INTO users (name, email, role) VALUES (?, ?, ?)",
                (name, email, role)
            )
            conn.commit()
            conn.close()
            flash("User added successfully!", "success")
            return redirect(url_for("list_users"))
        except sqlite3.IntegrityError:
            flash("Email already exists!", "error")
            return render_template("new_user.html")

    return render_template("new_user.html")

@app.route("/users/<int:user_id>")
def user_detail(user_id):
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    if user is None:
        abort(404, description="User not found")
    return render_template("user_detail.html", user=user)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", message=e.description), 404

@app.errorhandler(500)
def server_error(e):
    return render_template("500.html", message=e.description), 500

if __name__ == "__main__":
    app.run(debug=True)
