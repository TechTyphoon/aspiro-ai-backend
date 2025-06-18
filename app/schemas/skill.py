from pydantic import BaseModel

class SkillExtractionRequest(BaseModel):
    text: str

class SkillExtractionResponse(BaseModel):
    skills: list[str]
