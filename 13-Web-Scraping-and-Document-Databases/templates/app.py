# import necessary libraries
from flask import Flask, render_template, redirect
import scrape_info
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.test


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_info = db.mars.find()

    # return template and data
    #return render_template("index.html", forecasts=forecasts)
    return mars_info


if __name__ == "__main__":
    app.run(debug=True)