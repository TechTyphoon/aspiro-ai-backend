# Import the instance of our extractor from the file we just created
from app.services.skill_extractor import skill_extractor_instance

# Some sample text from a job description
sample_text = """
We are looking for a software engineer proficient in Python and JavaScript.
The ideal candidate should have experience with FastAPI and React.
Knowledge of Project Management and tools like Jira is a plus.
Experience with Google Cloud Platform (GCP) is also desired.
"""

print("\n--- Testing Skill Extraction ---")
print(f"Input Text: {sample_text}")

# Call the extract_skills method
extracted_skills = skill_extractor_instance.extract_skills(sample_text)

print("\n--- Extracted Skills ---")
print(extracted_skills)
print("\n--- Test Complete ---")
