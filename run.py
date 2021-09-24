import os
# as we are importing data as json
import json
# import the Flask class, and render_template function
from flask import Flask, render_template

# create instance of Flask class, naming convention is to call this app
app = Flask(__name__)


# route decorator - root directory - calls index function, which renders that file
@app.route("/")
def index():
    return render_template("index.html")


# path to about file, binds to a view, returns the rendered about.html page
# page_title variable displays the text assigned to it, in the html page
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# route and view for contact page
@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


# run the app using the arguments supplied below. defaults for IP and PORT
# debug=True only for development mode, change to =False for production 
if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)

