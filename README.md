# :fire: Human Program Flask Application :fire:

**Overview** 

The following application provides the means of checking human input to control states within a program. The **flask_app.py**  lauches a flask server which in turn constantly awaits requests from the **index.html** web page. When the user clicks the "submit" button on the web page, the flask_app.py launches the status setter script which changes the values within the JSON file. This simulates the "answer" from the user on the current state of the human program.

The following code has been tested on the https://www.pythonanywhere.com/ website, meaning to launch the code, you will have to install python and all of the corresponding dependancies:

1. Flask
2. Json

>Note that the following application is under development, meaning the code may be re-written to achieve certain functionality.

## TO-DO:

- Add "how to launch the application on the home server"
- Add "features" section