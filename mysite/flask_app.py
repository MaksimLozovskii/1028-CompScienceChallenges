
# A very simple Flask Hello World app for you to get started with...

from flask import Flask #imports the Flask function from flask
from flask import render_template #imports the render_template function from Flask
from flask import request #imports the request function from flask
from flask import redirect #imports the redirect function from flask
from flask import url_for #imports the url_for function from flask
from userDataSetter import storeUserData #import the storeUserData function from the userDataSetter
from userDataRetriever import sendEmailTo #import the sendEmailTo fucntion
import re #regex

regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

app = Flask(__name__) #Creates the flask app called app

# ROUTES
@app.route('/') #Defines the route at the default route
def serve_indexPage(): #Function that will run at the default route
    return render_template("index.html") #Renders an index.html file on the default route

@app.route('/captureForm') #Defines the captureForm route
def serve_captureForm(): #Function that will run at the /captureForm route
    return render_template("captureForm.html") #Renders the captureForm.html file at the this route

@app.route('/emailingPage')
def serve_emailingPage():
    return render_template("emailingPage.html") #renders the emailingPage.html at this route

@app.route('/success') #Defines the success route
def serve_success(): #Function that will run at the /success route
    return render_template("success.html") #Renders the success.html file at this route

@app.route('/error') #Defines the error route
def serve_error(): #Function that will run at the /error route
    return render_template("error.html") #Renders the error.html file at this route

# ROUTE METHODS
@app.route('/captureForm', methods=['POST'])
def serve_captureFormMethods():
        #Get user Email
        userEmailData = request.form['userEmail'] #Gets the data from the userEmail input
        userEmailLower = userEmailData.lower() #lowercases
        userEmail = userEmailLower.strip() #Strips the white space

        #Get user Forename
        userForenameData = request.form['userForename'] #Gets the data from the userForename input
        userForenameLower = userForenameData.lower() #lowercases
        userForename = userForenameLower.strip() #Strips the white space

        #Get user Surname
        userSurnameData = request.form['userSurname'] #Gets the data from the userSurname input
        userSurnameLower = userSurnameData.lower() #lowercases
        userSurname = userSurnameLower.strip() #Strips the white space

        if not regex.match(userEmail):
            return redirect(url_for("serve_error")) #Redirects to error.html file
        else:
            storeUserData(userEmail, userForename, userSurname) #store the data into JSON

            #On success
            return redirect(url_for("serve_success")) #Redirects the user to the success.html page on success

@app.route('/emailingPage', methods=['POST'])
def serve_emailingPageMethods():
        #Get user Email
        userEmailData = request.form['email-parameter']
        userEmailLower = userEmailData.upper() #lowercases
        userEmail = userEmailLower.strip() #Strips the white space

        if not regex.match(userEmail):
            return redirect(url_for("serve_error")) #Redirects to error.html file
        else:
            sendEmailTo(userEmail)

            return redirect(url_for("serve_success"))

