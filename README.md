# ASPIRO AI - Skill Extraction Service

ASPIRO AI is a full-stack application designed to be the backend engine for a personalized mentoring and career guidance platform. This service uses a powerful AI model to read any text and extract a list of technical skills and tools.

---

## About The Project

This project was built from scratch to serve as the core of an AI-powered guidance tool. It includes a robust backend API, a database for user management, and a machine learning service that can perform Named Entity Recognition (NER) to identify skills. A simple web UI is also included for easy interaction with the AI model.

---

## Features

* **RESTful API:** A scalable backend built with FastAPI.
* **Database Integration:** Uses SQLAlchemy and SQLite for user data persistence.
* **User Management:** Foundational endpoint for creating users.
* **AI-Powered Skill Extraction:** Leverages a Hugging Face Transformer model to extract skills from text.
* **Interactive UI:** A simple, user-friendly interface built with Gradio to demonstrate the AI's capability.

---

## Tech Stack

This project was built using the following technologies:

* **Backend:** Python, FastAPI
* **Database:** SQLite, SQLAlchemy
* **AI / ML:** PyTorch, Hugging Face Transformers
* **UI:** Gradio
* **Environment:** Python Virtual Environment, pip

---

## Getting Started

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/TechTyphoon/aspiro-ai-backend.git](https://github.com/TechTyphoon/aspiro-ai-backend.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd aspiro-ai-backend
    ```

3.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

4.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

5.  **Run the Backend API:**
    *Open a terminal and run:*
    ```sh
    uvicorn app.main:app --reload
    ```
    *The API will be available at `http://127.0.0.1:8000`.*

6.  **Run the Frontend UI:**
    *Open a **second** terminal and run:*
    ```sh
    python app_ui.py
    ```
    *The UI will be available at `http://127.0.0.1:7860`.*

---

## How to Use

1.  **API Documentation:** With the backend server running, navigate to `http://127.0.0.1:8000/docs` to view and interact with the API endpoints.
2.  **Web Interface:** With the UI running, navigate to `http://127.0.0.1:7860` to use the skill extractor through a simple web page.
   
