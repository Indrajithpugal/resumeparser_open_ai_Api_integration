import spacy
import re

# Load the English language model
nlp = spacy.load("en_core_web_sm")


# Define a function to extract the name section from a resume
def extract_name(resume_text):
    doc = nlp(resume_text)
    for entity in doc.ents:
        if entity.label_ == "PERSON":
            return entity.text
    return None


# Define a function to extract the education section from a resume
def extract_education(resume_text):
    education_keywords = [
        "education",
        "bachelor",
        "master",
        "phd",
        "university",
        "college",
        "degree",
    ]
    doc = nlp(resume_text)
    education = []
    for ent in doc.ents:
        if any(keyword in ent.text.lower() for keyword in education_keywords):
            education.append(ent.text)
    return "\n".join(education) if education else None


# Define a function to extract the experience section from a resume
def extract_experience(resume_text):
    experience_keywords = [
        "experience",
        "work",
        "employment",
        "internship",
        "job",
        "position",
    ]
    doc = nlp(resume_text)
    experience = []
    capture = False
    for line in resume_text.split("\n"):
        if any(keyword in line.lower() for keyword in experience_keywords):
            capture = True
        if capture:
            experience.append(line)
        if capture and line.strip() == "":
            break
    return "\n".join(experience).strip() if experience else None


# Define a function to extract contact information from a resume
def extract_contact_info(resume_text):
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    phone_pattern = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")

    doc = nlp(resume_text)
    email = None
    phone = None

    for token in doc:
        if email_pattern.match(token.text):
            email = token.text
        if phone_pattern.match(token.text):
            phone = token.text

    return {"email": email, "phone": phone}


# Example resume text
resume_text = """
John Doe
123 Main Street
City, State, ZIP
Email: john.doe@example.com
Phone: (123) 456-7890

Education:
Bachelor of Science in Computer Science
University of Somewhere, 2015-2019

Experience:
Software Engineer at Tech Company
June 2019 - Present
- Developed web applications using Python and JavaScript
- Collaborated with cross-functional teams to define project requirements
"""

# Extract the name from the resume
name = extract_name(resume_text)
print("Name:", name)

# Extract the education from the resume
education = extract_education(resume_text)
print("Education:", education)

# Extract the experience from the resume
experience = extract_experience(resume_text)
print("Experience:", experience)

# Extract the contact information from the resume
contact_info = extract_contact_info(resume_text)
print("Contact Info:", contact_info)
