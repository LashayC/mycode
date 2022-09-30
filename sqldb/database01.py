#!/usr/bin/python3

import sqlite3

# connects to database. If doesn't exist, will create one.
conn = sqlite3.connect('test.db')
print("Opened database successfully")
