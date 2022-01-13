import json

path = "/home/HAIRYCACTUS/mysite/assets/scheduled/config.json"

def change():
    fr = open(path, "r")
    data_object = json.load(fr)
    fr.close()
    data_object["userStatus"] = "answered"

    with open(path, "w") as fw:
        json.dump(data_object, fw)
        fw.close()