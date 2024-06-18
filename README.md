# Automated Course Development (ACD) Model

## Overview

Automated Course Development (ACD) Model is an AI-powered Streamlit application designed for SMEs, content creators, and educators. It facilitates the creation of comprehensive courses by dynamically generating course outlines and detailed content based on key parameters such as Course Name and Number of Modules. Additionally, the application generates complete courses with quiz questions, which can be conveniently downloaded as PDFs and PPTs. Users also have the option to modify the generated content as needed.

## Features

- Generate dynamic course outlines.
- Create complete courses with detailed content.
- Automatically generate quiz questions.
- Download the entire course and quizzes as PDFs and PPTs.
- Customize and modify the generated content.

## Getting Started

Follow these steps to run the ACD application on your local system.

### Step 1: Generate OpenAI API Key

1. Generate your OpenAI API key.
   
3. Store the key in a `.env` file with the following format:
   
   ```env
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

### Step 2: Set Up Your Environment

1. Ensure Python is installed on your system.
   
3. Open the command prompt.
   
5. Create a new virtual environment:
   
   ```sh
   python -m venv env
   ```

7. Activate the virtual environment:
   
   - On Windows:
     ```sh
     .\env\Scripts\activate
     ```
   
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```
     
9. Install the required libraries from the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

### Step 3: Run the Application

1. In the command prompt, navigate to the directory containing `app.py`.
   
3. Run the application:
   ```sh
   streamlit run app.py
   ```

### Step 4: Access the Application

- The application will open in your default web browser and should run smoothly.

## Upcoming Features

We are constantly working on improving the ACD application. Here are some upcoming features you can look forward to:

- **Integration of Educational Imagery**: Enhance the generated content with educational imagery for increased visual appeal and better learning.

## Thank You

Thank you for using the Automated Course Development Model. If you have any questions or need further assistance, feel free to reach out.
