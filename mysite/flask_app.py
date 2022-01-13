from flask import Flask, render_template, request, redirect, url_for
from statusSetter import change

path = "/home/HAIRYCACTUS/mysite/assets/scheduled/config.json"

# Setup the flask app.
app = Flask(__name__)

# Define flask routes
@app.route('/', methods=["GET", "POST"])
def serve_home():

    if request.method == "POST":
        change()
        return redirect(url_for("serve_success"))
    else:
        return render_template("index.html")

@app.route('/success')
def serve_success():
    return render_template("success.html")

# Program start
if __name__ == '__main__':
    app.run()


