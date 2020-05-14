#Create a view that accepts a birthdate as argument (in the format of your choice),
# and then display to the user the number of minutes he lived in his life.
from datetime import date
import flask
from flask import request

nameapp = flask.Flask(__name__)
today = date.today()
@nameapp.route('/name', methods = ["POST", "GET"]) #both post and get
def nametaker():
    datestring = ""
    if request.method == "POST":
        datestring = request.form.get("birthday")
        print(datestring)
        print("hello!")

    d1 = today.strftime("%Y-%m-%d")
    currentyear = int(d1[:4])
    dob = datestring[0:4]
    deltayear = int(currentyear) - 1990 #why couldn't I use int(dob)?

    html = flask.render_template("namepage.html", datestring=datestring, deltayear=deltayear)
    return html


if __name__ == "__main__":
    nameapp.run(debug=True)
