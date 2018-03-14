import pyrebase
import firebase_admin
from firebase_admin import credentials
from datetime import datetime

def motiondetect(a):


    config = {
    "apiKey": "enter yor data",
    "authDomain": "enter your data",
    "databaseURL": "enter your data",
    "storageBucket": "enter your data"
    }

    firebase = pyrebase.initialize_app(config)

    db = firebase.database()

    data = {"Blinked Eye at : ": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"name": a}
    db.child("eye-blink").push(data)
