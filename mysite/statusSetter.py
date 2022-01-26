import json

path = "/home/HAIRYCACTUS/mysite/assets/scheduled/config.json"

#Defines the function with param user
def change(user):
    #open the file as read
    fr = open(path, "r")
    #load the json object and store it in a data_object container
    data_object = json.load(fr)
    #close the file
    fr.close()
    #change the object field named as the passed parameter user to "answered"
    data_object[user] = "answered"

    #open the JSON file as write and dump the changes into it
    with open(path, "w") as fw:
        json.dump(data_object, fw)
        fw.close()
