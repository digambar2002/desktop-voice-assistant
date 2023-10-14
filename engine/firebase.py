# Not important in project you can safely delete it 

import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from utils import *
# Use a service account.
cred = credentials.Certificate('engine\\private_key.json')
app = firebase_admin.initialize_app(cred)
db = firestore.client()

# Read Data

# This function listens for any changes that happen in the database
def on_snapshot(doc_snapshot, changes, read_time):
    # Iterate over the changes
    for change in changes:
        if change.type.name == 'MODIFIED':
            # If a document is modified, print the new data
            # print(f"Document {change.document.id} was modified.")
            print("New data:", change.document.to_dict())

            # Get the result data from the document
            result = change.document.to_dict()

            # Check if incomingCall is True
            if result['incomingCall'] == True and result['pickupCall']== False:
                # Start a new thread to call the speak function
                speak("Boss, you have a phone call")
                if result['pickupCall'] == False:
                    speak("Can you pickup call")
                    val = input("enter Y and N")
                    if(val == "y"):
                        db.collection('phone').document('j1').update({'pickupCall':True})
                    else:
                        db.collection('phone').document('j1').update({'pickupCall':False})
                continue
            elif result['wakeup'] == True:
                speak("Boss How can i Assist You")

# Create a reference to the document to watch for changes
doc_ref = db.collection('phone').document('j1')

# Set the document snapshot listener with the on_snapshot function
doc_watch = doc_ref.on_snapshot(on_snapshot)

# Initialize speak function engine to avoid delay
initialize_engine()

# Keep the script running indefinitely
while True:
    pass



# ------------------------------------------------------------------------------------------------------------------

# This is bandwith eater code i conteniously send request to server this not good practice


# while True:
#     resuls = db.collection('phone').document('j1').get()

#     if resuls.exists:
#         print(resuls.to_dict())
#         incomingCall = resuls.to_dict()['incomingCall']
#         if(incomingCall == True):
#             print("value upadted")
#             speak("Boss you have a phone call")
#             break    

