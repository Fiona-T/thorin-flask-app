import os
# as we are importing data as json
import json
# import the Flask class, and render_template function, request method for form handling, flash for user feedback
from flask import Flask, render_template, request, flash
# import the env.py file if it exists
if os.path.exists("env.py"):
    import env

# create instance of Flask class, naming convention is to call this app
app = Flask(__name__)
# get the secret key from the env.py
app.secret_key = os.environ.get("SECRET_KEY")


# route decorator - root directory - calls index function, which renders that file
@app.route("/")
def index():
    return render_template("index.html")


# path to about file, binds to a view, returns the rendered about.html page
# page_title variable displays the text assigned to it, in the html page
# company used in html to display object information for each object in array in json file
@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


# route and view for contact page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
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

