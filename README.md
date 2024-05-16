# Automatic Course Content Generator (ACCG)

## Overview

Automatic Course Content Generator (ACCG) is an AI-powered Streamlit application designed for SMEs, content creators, and educators. It facilitates the creation of comprehensive courses by dynamically generating course outlines based on key parameters such as Course Name, Target Audience Education Level, Course Difficulty Level, and Course Credit. Additionally, the application generates complete courses with quiz questions, which can be conveniently downloaded as a PDF. Users also have the option to modify the generated content as needed.

## Features

- Generate dynamic course outlines.
- Create complete courses with detailed content.
- Automatically generate quiz questions.
- Download the entire course and quizzes as a PDF.
- Customize and modify the generated content.

## Getting Started

Follow these steps to run the ACCG application on your local system.

### Step 1: Generate OpenAI API Key

1. Generate your OpenAI API key.
2. Store the key in a `.env` file with the following format:
   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

### Step 2: Set Up Your Environment

1. Ensure Python is installed on your system.
2. Open the command prompt.
3. Create a new virtual environment:
   ```sh
   python -m venv env
   ```
4. Activate the virtual environment:
   - On Windows:
     ```sh
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source env/bin/activate
     ```
5. Install the required libraries from the `requirements.txt` file:
   ```sh
   pip install -r requirements.txt
   ```

### Step 3: Run the Application

1. In the command prompt, navigate to the directory containing `app.py`.
2. Run the application:
   ```sh
   streamlit run app.py
   ```

### Step 4: Access the Application

- The application will open in your default web browser and should run smoothly.

## Upcoming Features

We are constantly working on improving the ACCG application. Here are some upcoming features you can look forward to:

- **Download Course Content in PPT Format**: Users will soon be able to download the generated course content in PowerPoint (PPT) format. This feature will enhance readability and provide a more convenient learning experience for users.

## Thank You

Thank you for using the Automatic Course Content Generator. If you have any questions or need further assistance, feel free to reach out.
