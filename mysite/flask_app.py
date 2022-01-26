from flask import Flask, render_template, request, redirect, url_for
from statusSetter import change

path = "/home/HAIRYCACTUS/mysite/assets/scheduled/config.json"

# Setup the flask app.
app = Flask(__name__)

# Define flask routes
@app.route('/')
def serve_homePage():
    return render_template("index.html")

@app.route('/userOne', methods=["GET", "POST"])
def serve_userOne():

    if request.method == "POST":
        change("userOne")
        return redirect(url_for("serve_success"))
    else:
        return render_template("responsePage.html")

@app.route('/userTwo', methods=["GET", "POST"])
def serve_userTwo():

    if request.method == "POST":
        change("userTwo")
        return redirect(url_for("serve_success"))
    else:
        return render_template("responsePage.html")

@app.route('/userThree', methods=["GET", "POST"])
def serve_userThree():

    if request.method == "POST":
        change("userThree")
        return redirect(url_for("serve_success"))
    else:
        return render_template("responsePage.html")

@app.route('/userFour', methods=["GET", "POST"])
def serve_userFour():

    if request.method == "POST":
        change("userFour")
        return redirect(url_for("serve_success"))
    else:
        return render_template("responsePage.html")

@app.route('/userFive', methods=["GET", "POST"])
def serve_userFive():

    if request.method == "POST":
        change("userFive")
        return redirect(url_for("serve_success"))
    else:
        return render_template("responsePage.html")

@app.route('/success')
def serve_success():
    return render_template("success.html")

# Program start
if __name__ == '__main__':
    app.run()


