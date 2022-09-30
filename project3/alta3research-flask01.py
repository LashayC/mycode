#!/usr/bin/env python3
""" Flask API for Chinese Zodiac Animals """

# imports
from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

# create instance of Flask object
app = Flask(__name__)

# list for zodiac signs
zodiac_signs = [
    {
        "year" : [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020, 2032],
        "animal" : "Rat",
        "pic_url" : "https://www.rd.com/wp-content/uploads/2020/11/Rat.jpg?resize=1536,1536"
    },
    {
        "year" : [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021, 2033],
        "animal" : "Ox",
        "pic_url" : "https://www.rd.com/wp-content/uploads/2020/11/Ox.jpg?resize=1536,1536"
    }
]

# route to return JSON data
@app.route("/alldata")
def alldata():
    # jsonify returns legal JSON to user
    return jsonify(zodiac_signs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
