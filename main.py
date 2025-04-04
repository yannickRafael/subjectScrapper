import requests
from const import *
from bs4 import BeautifulSoup
from subject import Subject, SubjectEncoder
from utils import extract_course_code
import json
import re
from firebase import  save_subject

# const objects
session = requests.Session()

subjects = []

for course in courses.keys():
    full_url = partial_url + course + "/paginas-de-disciplinas"


    #generate session inside web page
    request = session.get(full_url)
    soup = BeautifulSoup(request.text, "html.parser")

    #get tables containing all subjects from curso webpage
    #each table contains a certain number of subjects
    tables = soup.find_all('table', class_='tab_lay')

    for table in tables:
        # get all links inside the table
        anchors = table.find_all('a')

        # iterate on each anchor
        for anchor in anchors:
            #get the content from the anchor. eg: <a>This is the content</a>
            name = re.sub(r'\s+', ' ', anchor.text).strip()

            #get the subject code inside the link
            code = extract_course_code(anchor['href'].strip())

            # create a subject instance
            foundSubject = Subject(name=name, identifier=code, ref=courses.get(course))
            subjects.append(foundSubject)


for subject in subjects:
    save_subject(subject)