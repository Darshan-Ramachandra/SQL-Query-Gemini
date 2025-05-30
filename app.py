from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from sqlite import initialize_database  # ← Add this line

# Initialize DB and table
initialize_database()  # ← Run setup on every app start

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    response = model.generate_content(prompt + "\n" + question)
    return response.text.strip()

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

prompt = """
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION, MARKS.
For example:
Example 1 - How many entries of records are present?
SQL: SELECT COUNT(*) FROM STUDENT;
Example 2 - Tell me all the students studying in Data Science class?
SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";
Do not use triple backticks or mention the word "sql" in the output.
"""

st.set_page_config(page_title="I can Retrieve any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input your question in English", key="input")
submit = st.button("Ask the question")

if submit:
    try:
        response = get_gemini_response(question, prompt)
        st.code(response, language='sql')
        data = read_sql_query(response, "student.db")
        st.subheader("Query Result:")
        for row in data:
            st.write(row)
    except Exception as e:
        st.error(f"Error: {e}")
