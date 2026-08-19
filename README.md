AI Agent \& RAG System



A tool-using AI agent that combines Google Gemini, LangGraph, LangChain, RAG (Retrieval-Augmented Generation) and FAISS Vector Database to answer both general questions and questions based on the RKT-MIL-STD-001 technical document.



🚀 Project Overview



This project demonstrates how an AI agent can dynamically decide which tool should be used according to the user's question.



The system supports two main workflows:



General Questions → Answered directly by the Gemini model.

RKT-MIL-STD-001 Questions → Relevant information is retrieved from the technical document using a FAISS vector database and then provided to Gemini through a RAG pipeline.

Architecture

&#x20;                        User

&#x20;                          │

&#x20;                          ▼

&#x20;                   LangGraph Agent

&#x20;                          │

&#x20;                 ┌────────┴────────┐

&#x20;                 │                 │

&#x20;                 ▼                 ▼

&#x20;       General Question       MIL-STD RAG

&#x20;            Tool                  Tool

&#x20;                 │                 │

&#x20;                 ▼                 ▼

&#x20;            Gemini             Retriever

&#x20;                                   │

&#x20;                                   ▼

&#x20;                             FAISS Vector DB

&#x20;                                   │

&#x20;                                   ▼

&#x20;                             Relevant Context

&#x20;                                   │

&#x20;                                   ▼

&#x20;                                 Gemini

🛠️ Technologies

Python

LangChain

LangGraph

Google Gemini

FAISS

RAG (Retrieval-Augmented Generation)

Python-dotenv

📁 Project Structure

ai-agent-project/

│

├── agent.py

├── tools.py

├── rag.py

├── create\_vector\_db.py

├── mil\_std\_document.py

├── main.py

├── requirements.txt

├── README.md

├── .gitignore

│

├── faiss\_index/        # Generated locally

└── .env                # Environment variables

🔍 RAG Pipeline



The RAG workflow follows these steps:



The user asks a question about the RKT-MIL-STD-001 document.

The AI agent selects the mil\_std\_rag\_tool.

The question is sent to the FAISS retriever.

Relevant document chunks are retrieved.

Retrieved content is combined into a context.

The context and question are passed to the RAG chain.

Gemini generates the final answer based on the retrieved information.



This approach helps the model answer questions using information from the provided technical document rather than relying only on its general knowledge.



🤖 AI Agent



The agent uses tools to determine how a question should be answered.



General Question Tool



Used for questions unrelated to the technical document.



User Question

&#x20;    ↓

general\_question\_tool

&#x20;    ↓

Gemini

&#x20;    ↓

Answer

MIL-STD RAG Tool



Used for questions related to RKT-MIL-STD-001.



User Question

&#x20;    ↓

mil\_std\_rag\_tool

&#x20;    ↓

FAISS Retriever

&#x20;    ↓

Relevant Documents

&#x20;    ↓

RAG Chain

&#x20;    ↓

Gemini

&#x20;    ↓

Answer

⚙️ Installation

1\. Clone the repository

git clone https://github.com/BugayTaskiran/ai-agent-project.git

cd ai-agent-project

2\. Create a virtual environment

python -m venv .venv

3\. Activate the virtual environment



Windows PowerShell:



.venv\\Scripts\\Activate.ps1

4\. Install dependencies

pip install -r requirements.txt

🔐 Environment Variables



Create a .env file in the project root:



GOOGLE\_API\_KEY=your\_api\_key\_here



Never commit your .env file or API keys to GitHub.



🗄️ Creating the Vector Database



The FAISS vector database is generated locally and is intentionally excluded from the repository.



Run:



python create\_vector\_db.py



This creates the local:



faiss\_index/



directory.



▶️ Running the Agent



After configuring the environment and creating the vector database:



python agent.py



The application will start an interactive terminal session:



Kullanıcı:



You can then ask questions such as:



RKT-MIL-STD-001 dokümanında çalışma sıcaklığı nedir?



or general questions such as:



Python nedir?



The agent determines which tool should handle the question.



🧠 Key Concepts Demonstrated



This project demonstrates practical implementation of:



AI Agents

Tool Calling

LangGraph

LangChain

Retrieval-Augmented Generation (RAG)

Vector Databases

FAISS

Document Retrieval

Prompt Templates

LLM Integration

Environment Variable Management

Conversational Memory

🔒 Security



Sensitive configuration files are excluded from version control using .gitignore.



The following files are intentionally not included in the repository:



.env

.venv/

faiss\_index/

\_\_pycache\_\_/

📌 Future Improvements



Possible improvements include:



Streaming responses

Improved document chunking

Metadata filtering

Source citation in RAG responses

Persistent conversation memory

Additional tools

Web search integration

Evaluation and retrieval quality metrics

More advanced LangGraph workflows

👨‍💻 Author



Alperen Bugay Taşkıran



Computer Engineering



GitHub: BugayTaskiran

