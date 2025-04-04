import firebase_admin
from firebase_admin import credentials, firestore
from config import key_path
from subject import Subject

# Initialize Firebase
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)

# Get Firestore database
db = firestore.client()

# Store subject in Firestore
def save_subject(subject: Subject):

    to_save = {
        "codigo": subject.identifier,
        "nome": subject.name,
        "cursoId": db.collection("cursos").document(subject.ref)

    }

    to_print = {
        "codigo": subject.identifier,
        "nome": subject.name,
        "cursoId": db.collection("cursos").document(subject.ref)

    }



    print(to_print)
    db.collection("cadeiras").add(to_save)