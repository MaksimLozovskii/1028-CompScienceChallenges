# :fire: Human Program Flask Application :fire:

**Overview** 

The following application provides the means of checking human input to control states within a program. The **flask_app.py**  lauches a flask server which in turn constantly awaits requests from the **responsePage.html** web page. When the user clicks the "submit" button on the web page, the flask_app.py launches the status setter script which changes the values within the JSON file. This simulates the "answer" from the user on the current state of the human program. 

The following code has been tested on the https://www.pythonanywhere.com/ website, meaning to launch the code, you will have to install python and all of the corresponding dependancies:

1. Flask
2. Json

>Note that the following application is under development, meaning the code may be re-written to achieve certain functionality.

## Implementation Guide
https://maksimlozovskii.pythonanywhere.com/

## Set-up
In order to use this application, you will need to:
1. Add your gmail email address and password to the userDataRetriever.py file instead of the "########" symbols
2. Enable less secure apps on that gmail account
3. Add path to the userData.json file into userDataRetriever.py script
4. Add path to the userData.json file into userDataSetter.py script
5. Within each of the .html files add path to css style files within the css folder (will depend on where you hosted the application)
