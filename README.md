# Resume-Application-Tracking-System
## Overview
The Resume Applicant Tracking System (ATS) is designed to streamline the recruitment process by evaluating and managing resumes efficiently. This system helps in matching candidates’ resumes with job descriptions, ensuring a more effective and organized hiring process.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Environment Variables](#environment-variables)
- [Contributing](#contributing)
- [License](#license)

## Features
1. **Resume Evaluation:** Upload a resume in PDF format and evaluate it against a provided job title and description.
2. **Detailed Insights:**
   1. Get detailed insights.
   2. Including match percentage.
   3. Role Alignment.
   4. Technical and Non-Technical Skills
   5. Educational Match Percentage
   6. Experience Match Percentage
   7. Keywords Matched
   8. Keywords Missing
   9. Final Thoughts
   10. Shortlisting Probability
   11. Recommendation
   12. Alternative Job Titles
4. **Interview Questions Generation:** Generate over 50 interview questions with sample answers tailored to the job title and description.

## Requirements
  Before you begin, ensure you have the following installed:
  * Python 3.7 or later
  * pip package manager
  * Google API key for Generative AI

## Installation
Follow these steps to set up the project on your local machine:
1. **Clone the Repository:**
     ```javascript
      git clone https://github.com/ahmedhassan29290/Resume-Application-Tracking-System.git
      cd resume-ats-tracking-system
      ```
2. **Create a Virtual Environment (optional but recommended):**
     ```javascript
      python -m venv venv
      source venv/bin/activate  # On Windows: venv\Scripts\activate
      ```
3. **Install the Required Packages:**
     ```javascript
       pip install -r requirements.txt
     ```
4. **Set Up Environment Variables:**
     * Create a **.env** file in the root directory.
     * Generate an OpenAI API key by signing up or logging in at OpenAI Platform.
     * Add your Google API key to the **.env** file:
     ```javascript
      GOOGLE_API_KEY=your_google_api_key
     ```

## File Structure
The project is structured as follows:
- **`app.py`**: This is the entry point for the Streamlit app. It handles the user interface and interactions.
- **`pdf_utils.py`**: Contains functions for processing and extracting text from PDF files.
- **`gemini_client.py`**: Manages interactions with the Google Generative AI, sending prompts, and receiving responses.
- **`prompts.py`**: Houses templates for prompts used in AI interactions, including those for generating interview questions.
- **`config.py`**: Loads environment variables and configuration settings.
- **`requirements.txt`**: Lists all Python packages that need to be installed.
- **`.env`**: A file to store environment variables. Not included in version control.
- **`README.md`**: Project documentation.






     

  
