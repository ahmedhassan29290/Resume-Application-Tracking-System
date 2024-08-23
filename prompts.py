def get_interview_question(title,description):
    """
    Generate the interview question for evaluating a resume.
    
    Parameters:
    - title (str): Job title.
    - description (str): Job description.
    
    Returns: 
    - str: Formatted interview question for evaluation.
    """
    prompt  = """
        You are an experienced Technical Human Resource Manager. Your task is to thoroughly evaluate the provided resume against the job title {title} and the detailed job description {description}.
        Give the 50 + Interview Question with answers which is possibility to asked in the interview, technical and non technical question need to includes 
        """
    return prompt.format(title=title, description=description)
    

def get_detailed_prompt(title, description):
    """
    Generate the detailed prompt for evaluating a resume.

    Parameters:
    - title (str): Job title.
    - description (str): Job description.

    Returns:
    - str: Formatted detailed prompt for evaluation.
    """
    prompt  = """
        As an experienced Technical Human Resource Manager, your expertise is requested to conduct a thorough evaluation of a candidate's resume in relation to a specific {title} and detailed {description}. Your evaluation should encompass the following aspects:

        1. **Overall Match Percentage:** Determine the percentage of alignment between the candidate's resume and the provided {description}.
        2. **Role Alignment:** Evaluate how well the candidate’s skills, strengths, weaknesses, and areas for improvement align with the role. Consider their cultural fit and overall suitability for the position.
        3. Technical skills and non technical skills
        4. **Educational Match:** Assess the percentage of the candidate’s educational background that meets the requirements specified in the {description}. Highlight any gaps.
        5. **Experience Match:** Calculate the percentage of the candidate’s experience that aligns with the {description}. Identify any significant areas of experience that are present or missing.
        6. **Keywords Matched:** List the key terms and phrases from the {description} that are present in the resume with overall percentage.
        7. **Keywords Missing:** Identify any critical keywords or phrases from the {description} that are not present in the resume with overall percentage.
        8. **Final Thoughts:** Provide a comprehensive overview of the candidate’s fit for the role, including any additional observations or considerations.
        9. **Shortlisting Probability:** Estimate the likelihood of the candidate being shortlisted for the position based on your evaluation with explanation.
        10. **Recommendation:** Offer your recommendation regarding the candidate’s suitability for the role.
        11. **Alternative Job Titles:** Suggest other job titles for which this resume might be a good fit, based on the candidate’s qualifications and experience.
    """
    return prompt.format(title=title, description=description)

