import json #Imports the whole JSON file

path = "#################" #Defines the path the JSON file
listObj = [] #Object holder array

def storeUserData(email, forename, surname):
    #Read JSON
    with open(path) as fp: #open the JSON file as fp
        listObj = json.load(fp) #load the fp JSON object data into the listObj array

    #Define the JSON object to be stored into the JSON file
    user_data = {"email" : email, "forename" : forename, "surname" : surname}

    existsFlag = False #set the flag to be initially False
    for i in listObj["userRecords"]: #loop through all JSON objects within the listObj array
        json_str = json.dumps(i) #Get the string version of the object in the array
        json_object = json.loads(json_str) #Get the JSON object
        if(json_object["email"] == email): #If the email attribute within the JSON object equals the email attribute we are trying to add to JSON
            existsFlag = True #Make the flag equal to true (means that the JSON file already has an object with such email address"

    if(existsFlag != True): #If the flag is false

        listObj["userRecords"].append(user_data) #append the JSON object we created to the listObj array

        #Do a dump to the JSON file
        with open(path, "w") as file: #Open the JSON file with write as file
            json.dump(listObj, file, indent = 4, separators = (',',': ')) #Dump the object into the file, with indents and separators (helps readability)
            file.close() #close the file
        print("User added") #if successful, print that user is added into the console
    else:
        print("User already exists") #If unseccessful, type that he user already exists
storeUserData("hello@world", "HELLO", "WORLD")