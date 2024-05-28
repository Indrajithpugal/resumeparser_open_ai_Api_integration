import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")


# Define a function to extract the name section from a resume
def extract_name(resume_text):
    doc = nlp(resume_text)
    name = None
    print(doc.ents)
    for entity in doc.ents:
        print(entity.label_, entity.text)
        # if entity.label_ == "PERSON":
        #     name = entity.text
        #     break
    return name


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
