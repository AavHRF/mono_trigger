# Header file to have functions in to keep app clean
import requests
from bs4 import BeautifulSoup

def debug_log(text):
    with open("debug.log", "a") as fstream:
        fstream.write(f"{text}\n")

def sanitize(text):
    return text.lower().replace(" ", "_")

def verify_nation(name):
    headers = {
        "User-Agent" : name
    }
    response = False
    try:
        r = requests.get(f"https://nationstates.net/cgi-bin/api.cgi?nation={name}", headers=headers)
        r.raise_for_status()
        response = True

    except Exception as e:
        debug_log(e)
        debug_log("Nation does not exist.")
        print("Nation does not exist.")

    return response

def watch_region(name, agent):
    headers = {
        "User-Agent" : agent
    }
    r = requests.get(f"https://nationstates.net/cgi-bin/api.cgi?region={name}&q=lastupdate", headers=headers)

def create_trigger_list(file):
    region_list = list()
    with open(f"{file}", "r") as li:
        region_list = li.read().split(",")
        return region_list