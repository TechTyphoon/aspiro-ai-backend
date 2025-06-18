from fastapi import APIRouter

from app.schemas.skill import SkillExtractionRequest, SkillExtractionResponse
# Import the instance of our AI service
from app.services.skill_extractor import skill_extractor_instance

router = APIRouter()

@router.post("/extract/", response_model=SkillExtractionResponse)
def extract_skills_from_text(
    request_body: SkillExtractionRequest
):
    """
    Accepts a block of text and returns a list of skills extracted by the AI model.
    """
    # Get the text from the incoming request
    text_to_analyze = request_body.text

    # Use our AI service to extract skills
    extracted_skills = skill_extractor_instance.extract_skills(text_to_analyze)

    # Return the skills in the correct response format
    return {"skills": extracted_skills}
