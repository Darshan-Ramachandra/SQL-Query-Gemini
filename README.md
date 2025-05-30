# Gemini SQL Query Retriever :crystal_ball:

## Overview :mag:
An intelligent application that uses Google Gemini to convert English questions into SQL queries and retrieve relevant data from a SQLite database. Built using **Streamlit** for an interactive UI and **Google Gemini API** for natural language processing.

## Features :sparkles:
- **Natural Language to SQL Conversion**
  - Ask questions like "How many students are in Data Science?"
  - Gemini API converts this into SQL syntax.

- **SQLite Integration**
  - Reads and executes generated queries from a local database.

- **Auto Initialization**
  - Automatically creates a database and populates it with sample data on the first run.

- **Streamlit UI**
  - Easy-to-use interface for asking questions and viewing SQL query results.

## Technologies Used

| Technology         | Description                                                             |
|--------------------|-------------------------------------------------------------------------|
| **Streamlit**      | Python framework for building interactive web apps.                     |
| **SQLite**         | Lightweight, disk-based database for storing student records.           |
| **Google Gemini API** | Converts English questions to SQL queries using AI.                  |
| **Python (dotenv)**| Loads environment variables securely.                                   |

## Setup Instructions :wrench:

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/gemini-sql-query-retriever.git
```

### 2. Navigate to the Project Directory

```bash
cd gemini-sql-query-retriever
```
### 3. Create a virtual env

```bash
cd python -m venv venv
cd ./venv/Scripts/Activate
```

### 4. Install Dependencies

Ensure you have Python 3.8+ installed.

```bash
pip install -r requirements.txt
```


### 5. Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```env
GOOGLE_API_KEY=<your-gemini-api-key>
```

### 6. Run the App

```bash
streamlit run app.py
```

This will launch a local server where you can interact with the app.

## How to Get Your Google Gemini API Key :key:

1. Go to the [Google AI Studio](https://makersuite.google.com/app).
2. Log in with your Google account.
3. Click on your profile icon (top right) > **API Keys**.
4. Generate a new API key and copy it.
5. Paste it into your `.env` file like so:

```env
GOOGLE_API_KEY=your-generated-api-key
```

> Make sure billing is enabled and API access is active in your Google Cloud project.

## Project Structure :file_folder:

```
.
├── app.py              # Main Streamlit app
├── sql.py              # Alternate app version (can be ignored if using app.py)
├── sqlite.py           # DB initialization script
├── student.db          # SQLite database (auto-generated)
├── .env                # Contains your API key
└── requirements.txt    # Python dependencies
```

## Contributing :handshake:

### 1. Fork the Repository

Click the "Fork" button in GitHub to copy the repo to your account.

### 2. Clone Your Fork

```bash
git clone https://github.com/<your-username>/gemini-sql-query-retriever.git
```

### 3. Create a Branch

```bash
git checkout -b feature-branch-name
```

### 4. Commit and Push

```bash
git add .
git commit -m "Added new feature or fix"
git push origin feature-branch-name
```

### 5. Submit a Pull Request

Go to the original repository and open a PR from your fork.

---

:star: If you like this project, give it a star on GitHub!