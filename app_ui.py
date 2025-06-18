import gradio as gr
import requests
import json

# The URL of the FastAPI backend you have running
API_URL = "http://127.0.0.1:8000/api/v1/skills/extract/"

def extract_skills_from_api(text_input):
    """
    This function takes text, sends it to our FastAPI backend,
    and returns the list of skills.
    """
    if not text_input:
        return "Please enter some text to analyze."

    # The payload must match our SkillExtractionRequest schema
    payload = {"text": text_input}

    try:
        # Make the POST request to our API
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        # Parse the JSON response
        data = response.json()
        skills = data.get("skills", [])

        # Format the output for better display
        if skills:
            return "\n".join(f"- {skill}" for skill in skills)
        else:
            return "No skills were identified."

    except requests.exceptions.RequestException as e:
        return f"Error connecting to the API: {e}"
    except json.JSONDecodeError:
        return "Error: Could not decode the response from the API."


# Create the Gradio interface
iface = gr.Interface(
    fn=extract_skills_from_api,
    inputs=gr.Textbox(
        lines=15, 
        label="Job Description or Resume Text",
        placeholder="Paste a job description or resume text here..."
    ),
    outputs=gr.Textbox(
        label="Extracted Skills"
    ),
    title="ASPIRO AI - Skill Extractor",
    description="An AI-powered tool to extract key skills from any text. Powered by Hugging Face Transformers and a FastAPI backend.",
    allow_flagging="never"
)

# Launch the web application
if __name__ == "__main__":
    print("Launching Gradio UI...")
    iface.launch()
