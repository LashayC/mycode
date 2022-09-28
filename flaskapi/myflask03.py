#!/usr/bin/python3

#imports
from flask import Flask, redirect, url_for
app = Flask(__name__)

# URL route admin
@app.route("/admin")
def hello_admin():
    return "Hello Admin"

# URL route with parm
@app.route("/guest/<guesty>")
def hello_guest(guesty):
    return f"Hello {guesty} Guest"
    #V2 FORMATTER - return "Hello {} Guest".format(guesty)
    #OLD FORMATTER - return "Hello %s as Guest" % guesty

# URL route with param <user>
@app.route("/user/<name>")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name == "admin":
        # return a 302 response to redirect to /admin
        # use url_for function to redirect. 1st param= name of function, 2nd, etc param = keyword args for each var part of URL
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response ot redirect to /guest/<guesty>
        return redirect(url_for("hello_guest", guesty = name))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
