# ATS Analyzer App

## Overview
The **ATS Analyzer App** is a Flask-based web application designed to help job seekers analyze their resumes for **ATS (Applicant Tracking System) friendliness**. The app extracts key details from resumes and presents them in **JSON format**, allowing users to optimize their resumes for better visibility in recruitment processes.

## Features
- **Upload Resume**: Accepts resumes in **PDF format**.
- **Extracts Key Information**:
  - Full Name
  - Email ID
  - GitHub Portfolio (if available)
  - LinkedIn Profile (if available)
  - Employment Details (Job titles, company names, duration, key responsibilities)
  - Technical Skills (Programming languages, frameworks, tools, etc.)
  - Soft Skills (Communication, teamwork, leadership, etc.)
- **Uses OpenAI's GPT model** to intelligently extract structured data from resumes.
- **Displays extracted data in JSON format**.

## Tech Stack
- **Backend**: Flask (Python)
- **AI Integration**: OpenAI GPT (for resume parsing)
- **PDF Processing**: PyPDF
- **Configuration Management**: YAML

## Installation & Setup

### Prerequisites
Make sure you have **Python 3.7+** installed.

### 1. Clone the Repository
```sh
$ git clone https://github.com/DevangVamja/ATS-Analyzer-OpenAI.git
$ cd ATS-Analyzer-OpenAI
```

### 2. Install Dependencies
```sh
$ pip install -r requirements.txt
```

### 3. Configure OpenAI API Key
- open the **config.yaml** file in the root directory.
- Add your **OpenAI API key** in the following format:

```yaml
OPENAI_API_KEY: "your_openai_api_key_here"
```

### 4. Run the Application
```sh
$ flask --app app.py run
```

### 5. Access the App
Go to your browser and open:
```
http://localhost:5000
```

## How to Use
1. Open the web app.
2. Upload your resume in **PDF format**.
3. Click on the **Upload** button.
4. View extracted information in **JSON format**.

## Example Output
```json
{
  "Full Name": "John Doe",
  "Email ID": "john.doe@example.com",
  "GitHub Portfolio": "https://github.com/johndoe",
  "LinkedIn Profile": "https://linkedin.com/in/johndoe",
  "Employment Details": [
    {
      "Company": "ABC Corp",
      "Position": "Software Engineer",
      "Duration": "Jan 2020 - Present",
      "Responsibilities": "Developed scalable web applications."
    }
  ],
  "Technical Skills": ["Python", "Flask", "SQL", "Machine Learning"],
  "Soft Skills": ["Teamwork", "Leadership", "Problem-solving"]
}
```

## Troubleshooting
- **Issue: OpenAI API errors**
  - Ensure your **API key** is correctly added in **config.yaml**.
  - Check your **OpenAI API usage limits**.
- **Issue: Flask app not starting**
  - Run `flask --app app.py run` instead of `python app.py`.
  - Ensure all dependencies are installed with `pip install -r requirements.txt`.
- **Issue: File upload not working**
  - Ensure the **uploads directory** (`__data__`) exists.
  - Only **PDF files** are supported.

## Future Enhancements
- Add support for **DOCX file formats**.
- Implement **resume scoring** based on ATS criteria.
- Improve **skill extraction** using advanced NLP techniques.

## Contributing
We welcome contributions! Feel free to submit pull requests or open issues if you find any bugs or have feature suggestions.

---
**Developed by**: Devang Vamja

