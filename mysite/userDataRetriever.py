import json #imports Json
import smtplib #imports smtplib

path = "/home/####/mysite/assets/userData/userData.json" #path to the userData.json file
listObj = [] #Json object array holder

def sendEmailTo(email): #function definition that takes the user email and sends an email to the provided address

    email = email.strip()
    email = email.lower()
    #Read JSON
    with open(path) as fp: #Open the json file at the provided path as fp
        listObj = json.load(fp) #load the contents of the JSON file into the object array

    for i in listObj['userRecords']: #loop throught the userRecords array stored in the listObj array
        json_str = json.dumps(i) #get the string version of the array of objects

        json_object = json.loads(json_str) #load the array into an object

        if(json_object["email"] == email): #if the email attribute value matches the parsed data
        #send an email
            def send_email(to):
                myEmail = "####"
                myPass = "####"
                subject = "Hello " + json_object["forename"] + "_" + json_object["surname"]
                body = "Hello, this is automatic"
                email_text = "Subject: {}\n\n{}".format(subject, body)

                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(myEmail, myPass)
                server.sendmail(myEmail, to, email_text)
                server.quit()
            send_email(email)

            # on success
            print("email sent")
        else:
            print("email not found")



