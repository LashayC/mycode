#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

#create a URL route with a rule paramater 
@app.route("/hello/<name>")
def hello_name(name):
    return f"Hello {name}"
    # V2 STYLE STRING FORMATTER - RETURN "Hello ()".format(name)
    # OLD STYLE STRING FORMATTER - return "Helllo %s!" % name

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224) # runs the application
