# We are using a high-level "pipeline" from Hugging Face.
# It handles all the complex stuff for us.
from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification

class SkillExtractor:
    def __init__(self):
        """
        Loads the pre-trained model and tokenizer when a new SkillExtractor is created.
        """
        print("Loading AI model for skill extraction... This may take a moment.")

        # This is the name of a model from the Hugging Face Hub, specifically
        # fine-tuned for Named Entity Recognition (NER).
        model_name = "dslim/bert-base-NER"

        # Load the tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForTokenClassification.from_pretrained(model_name)

        # Create the NER pipeline
        # We use "aggregation_strategy" to group parts of a skill together
        # (e.g., "Project" and "Management" become "Project Management").
        self.ner_pipeline = pipeline(
            "ner",
            model=model,
            tokenizer=tokenizer,
            aggregation_strategy="simple"
        )
        print("AI Model loaded successfully.")

    def extract_skills(self, text: str) -> list[str]:
        """
        Takes a block of text and returns a list of unique skills found.
        """
        # Run the text through our AI pipeline
        ner_results = self.ner_pipeline(text)

        # The model returns entities like "Organization" (ORG), "Person" (PER), etc.
        # Many technical skills are identified as "Miscellaneous" (MISC).
        # We will extract these.

        skills = []
        for entity in ner_results:
            # We are interested in MISC entities, as they often contain skills
            if entity['entity_group'] == 'MISC':
                # Add the found skill to our list, removing extra spaces
                skills.append(entity['word'].strip())

        # Return a list of unique skills by converting to a set and back to a list
        return list(set(skills))

# This creates a single, reusable instance of our extractor
skill_extractor_instance = SkillExtractor()
