import firebase_admin
from firebase_admin import credentials, firestore
from config import key_path
from subject import Subject

# Initialize Firebase
#key path is a variable containing the path to the json key file
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

# Get Firestore database
db = firestore.client()

# Store subject in Firestore
def save_subject(subject: Subject):

    # create document to store
    to_save = {
        "codigo": subject.identifier, # subject code
        "nome": subject.name, # subject name
        "cursoId": db.collection("cursos").document(subject.ref) # course reference

    }

    # save document to collection "cadeiras"
    db.collection("cadeiras").add(to_save)