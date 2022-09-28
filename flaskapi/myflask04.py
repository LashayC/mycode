#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for ea impoer
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template

app = Flask(__name__)

## This is where we want to redirect users to
@app.route("/success/<name>")
def success(name):
    return f"Welcome {name}\n"

# This is a landing poit for users (a start)
@app.route("/") # user can land at "/"
@app.route("/start") # or user can land at "/start"
def start():
    return render_template("postmaker.html") # look for templates/postmaker.html you just created

# This is where postmaker.html POSTs data to 
# A user could also browser (GET) to this location
@app.route("/login", methods = ["POST", "GET"])
def login():
    #POST would likely come from a user interacting with postmaker.html
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assisgned via the POST in html doc
            user = request.form.get("nm") # grab the value of nm from the post
        else: # if a user sent a post w/out nm then assign value defaultuser
            user = "defaultuser"
    # GET would likel come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned a s a parameter = value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed ...
            user = "defaultuser"
    return redirect(url_for("success", name = user)) # pass back to /sucess with val for name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
