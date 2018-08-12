# import necessary libraries
from flask import Flask, render_template, redirect
from scrape_mars import scrape
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["marsdb"]
mycol = mydb["mars"]


# create route that renders index.html template and finds documents from mongo
@app.route("/")
def home():

    # Find data
    mars_info = mycol.find_one()
    # return template and data
    return render_template("index.html", mars=mars_info)

@app.route("/scrape")
def scrape_info():
    scrape()
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)