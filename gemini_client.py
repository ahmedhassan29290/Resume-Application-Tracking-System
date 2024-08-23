import google.generativeai as genai
from config import GOOGLE_API_KEY

class GeminiClient:
    def __init__(self):
        genai.configure(api_key=GOOGLE_API_KEY)
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def get_response(self, input_text, pdf_content, prompt):
        """
        Generate a response using the Gemini model.

        Parameters:
        - input_text (str): User input text.
        - pdf_content (list): List containing PDF content encoded in base64.
        - prompt (str): Prompt text for the Gemini model.

        Returns:
        - str: Response text from the model.
        """
        response = self.model.generate_content([input_text, pdf_content[0], prompt])
        return response.text
