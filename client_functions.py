# Header file to have functions in to keep app clean
import requests

def debug_log(text):
    with open("debug.log", "a") as fstream:
        fstream.write(f"{text}")

def sanitize(text):
    return text.lower().replace(" ", "_").replace("\n", "")

def verify_nation(name):
    headers = {
        "User-Agent" : name
    }

    try:
        r = requests.get(f"https://nationstates.net/cgi-bin/api.cgi?nation={name}", headers=headers)

        # If nation does not exist, no-go
        if r.text.find("404") != "-1":
            debug_log("Nation does not exist.")
            print("Nation does not exist.")
            response = False

        else:
            response = True

    except Exception as e:
        debug_log(e)

    return response

def watch_nation(name, agent):
    print("")

def create_trigger_list(file):
    with open(f"{file}", "r") as li:
        print("")