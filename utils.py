from urllib.parse import urlparse

#this is a function to extract the subject code from the url
def extract_course_code(url: str) -> str:

    # Parse the URL to get the path
    path = urlparse(url).path

    # Split the path into parts and find the "disciplinas" segment
    parts = path.split('/')
    if "disciplinas" in parts:
        index = parts.index("disciplinas")
        if index + 1 < len(parts):
            return parts[index + 1]  # The next segment after "disciplinas" is the course code

    return None  # Return None if the course code is not found
