from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["UPLOAD_PATH"] = "static/images"

@app.route("/")
def main():
    return render_template("main.html") 

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/register", methods=["GET"])
def register():
    name = request.args.get("name")
    number = request.args.get("number")
    email = request.args.get("email")
    return render_template("register.html", name = name, number = number, email = email)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        error = None
        if request.form["username"] == "user"  and request.form["password"] == "password":
            return render_template("dashboard.html")
        else:
            error = "Wrong user name or password!"
            return render_template("login.html", error = error)
    else:
        return render_template("login.html", username = None, password = None)

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config["UPLOAD_PATH"], file.filename))
    return "uploaded successfully"

if __name__ == "__main__":
    app.run(debug=True)

#end of code
