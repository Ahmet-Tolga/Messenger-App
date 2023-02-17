import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("messenger-fb819-firebase-adminsdk-i722a-1010edd682.json")
firebase_admin.initialize_app(cred,{"databaseURL":"https://messenger-fb819-default-rtdb.firebaseio.com"})
users=db.reference("/users")
messages=db.reference("/messages")
def add_user(name,password):
    users.push({"name":name,"password":password})
def add_message(message,username,date):
    messages.push({"message":message,"username":username,"date":date})
def get_user():
    return users.get().values()
def get_message():
    return messages.get().values()
def get_control():
    return messages.get()
def get_len_of_messages():
    if(get_control()!=None):
        return len(get_message())

