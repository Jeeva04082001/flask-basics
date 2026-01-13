# //---Learn Basics--------

from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"


# -----------------------------------

@app.route("/users", methods = ["GET"])   
def get_users():
    return "User list" 


@app.route("/users", methods=["POST"])
def create_user():
    return "user created"

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return f"User ID: {user_id}"

#================================================

# -----------------------------------

# request.form is used to access data submitted through HTML forms using POST requests,
# while request.args is used for query parameters and request.json for JSON payloads.


# | Method         | Used for           | Example                |
# | -------------- | ------------------ | ---------------------- |
# | `request.args` | Query params (GET) | `/register?name=jeeva` |
# | `request.form` | Form data (POST)   | HTML form submit       |
# | `request.json` | JSON body          | API requests           |

#================================================

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f" User {name} register with {email}"
    return "register page"


# -----------------------------------


@app.route("/api/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        data = request.json

        username = data.get("username")
        password = data.get("password")

        if username == "admin" and password == "1234":
            return jsonify({"message" : "Login successfully"})
        
        return jsonify({"message": "Invalid credential"}),401
    return jsonify({"message": "send post request to login"})

# ===== Query Parameter======================================

# -------- http://127.0.0.1:5000/searching?name=jee&age=25 ---------------------------

@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        keyword = request.form.get("keyword")
        return f"Advance search for: {keyword}"
    query = request.args.get("q")
    return f" Searching for : {query}"

# ===========================================

@app.route("/searching")
def searching():
    name = request.args.get("name")
    age = request.args.get("age")
    return f"Name:{name}, Age:{age}"

# -----------------------------------



if __name__ == "__main__":
    app.run(debug=True)









# flask_mysql_app/
# │
# ├── app/
# │   ├── __init__.py        ← app creation
# │   ├── config.py          ← MySQL config
# │   ├── extensions.py      ← DB init
# │   ├── models.py          ← DB models
# │   └── routes.py          ← APIs / routes
# │
# ├── run.py                 ← app start file
# ├── requirements.txt
# └── venv/










