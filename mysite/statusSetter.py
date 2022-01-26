import json

path = "/home/HAIRYCACTUS/mysite/assets/scheduled/config.json"

<<<<<<< HEAD
def change():
    fr = open(path, "r")
    data_object = json.load(fr)
    fr.close()
    data_object["userStatus"] = "answered"
=======
def change(user):
    fr = open(path, "r")
    data_object = json.load(fr)
    fr.close()
    data_object[user] = "answered"
>>>>>>> 662d463 (ADD new links and routes for flask_app.py :fire:)

    with open(path, "w") as fw:
        json.dump(data_object, fw)
        fw.close()