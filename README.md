🦜 Chat2SQl: Natural Language Interface for SQL Databases

Chat2SQL is a Streamlit app powered by LangChain and Groq LLM that lets you chat with your database using natural language.
It supports both SQLite (student.db) and MySQL connections, making it easy to query, explore, and analyze data without writing SQL manually.

🚀 Features

✅ Choose your database: SQLite or MySQL

✅ Natural language to SQL with LangChain Agents

✅ Powered by Groq LLM (Llama3-8b-8192)

✅ Streamlit UI with chat history

✅ Secure credential handling with sidebar inputs

✅ Clear history option for fresh conversations

🛠️ Tech Stack

Python 3.10+

Streamlit – UI for chat interaction

LangChain – SQL agent & toolkits

Groq API – LLM backend (Llama3)

SQLite – Local DB option

MySQL – Remote DB option via mysql-connector

SQLAlchemy – Database connection layer

📦 Installation

Clone this repository:

git clone https://github.com/your-username/chatdb.git
cd chatdb


Create a virtual environment & install dependencies:

pip install -r requirements.txt


Example requirements.txt:

streamlit
langchain
sqlalchemy
mysql-connector-python
langchain-groq


Place your SQLite DB (student.db) inside the project folder
OR provide MySQL credentials in the sidebar when running.

▶️ Usage

Run the app with:

streamlit run app.py


Then open http://localhost:8501
 in your browser.

Choose SQLite (student.db) or MySQL in the sidebar

Provide your Groq API Key

Ask questions like:

"Show all students with marks greater than 80"

"Count the number of students in section A"

📷 Screenshot

(You can add a screenshot of the Streamlit app here)

🔮 Roadmap

 Add support for PostgreSQL

 Visualize query results with charts

 Export query outputs as CSV/Excel

 Add authentication layer for multi-user access

🙌 Acknowledgements

LangChain

Streamlit

Groq
