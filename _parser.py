from openai import OpenAI
import yaml

api_key = None
CONFIG_PATH = r"config.yaml"

with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['OPENAI_API_KEY']

def extractor(resume_data):

    prompt = '''
        You are an AI resume parser specializing in extracting key information from resumes with high accuracy. Given a resume, your task is to extract and structure the following details in **JSON format only**:  

        1. **Full Name**  
        2. **Email ID**  
        3. **GitHub Portfolio (if available)**  
        4. **LinkedIn Profile (if available)**  
        5. **Employment Details** (including job titles, company names, duration, and key responsibilities)  
        6. **Technical Skills** (programming languages, frameworks, tools, etc.)  
        7. **Soft Skills** (communication, teamwork, leadership, etc.)  

        ### **Guidelines:**  
        - Maintain proper formatting and ensure correctness.  
        - If any field is missing in the resume, return `null` for that key.  
        - Extract skills **intelligently** by categorizing them into technical and soft skills.  
        - Focus on **structured, concise, and relevant** information.  

        **Output:**  
        Return the extracted details **strictly** in JSON format, without any additional text.  
    '''

    openai_client = OpenAI(
        api_key = api_key
    )    

    
    response = openai_client.chat.completions.create(
        model="gpt-4o",  # Use "gpt-4" if available for better accuracy
        messages=[
            {"role": "developer", "content": prompt},
            {"role": "user", "content": resume_data}  # Assuming `resume_data` is the raw resume text
        ],
        temperature=0.0,
        max_tokens=2000 # Increase this value if the response is too short
    )
        
    data = response.choices[0].message.content

    #print(data)
    return data