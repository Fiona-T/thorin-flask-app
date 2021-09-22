import os
# import the Flask class, and render_template function
from flask import Flask, render_template

# create instance of Flask class, naming convention is to call this app
app = Flask(__name__)


# route decorator - root directory - calls index function, which renders that file
@app.route("/")
def index():
    return render_template("index.html")


# path to about file, binds to a view, returns the rendered about.html page
@app.route("/about")
def about():
    return render_template("about.html")


# route and view for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/careers")
def careers():
    return render_template("careers.html")


# run the app using the arguments supplied below. defaults for IP and PORT
# debug=True only for development mode, change to =False for production 
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

