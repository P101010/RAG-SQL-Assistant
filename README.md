# RAG SQL Assistant

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [License](#license)

## Overview

The **RAG SQL Assistant** is a powerful Retrieval-Augmented Generation (RAG) tool designed to help users to interact with SQL databases through natural language and retrieve results leveraging LangChain, OpenAI embeddings, GPT-4o and Postgres database.

## Features

- **Natural Language Processing**: Interact with SQL databases using natural language.
- **Chat Memory**: Maintains context across interactions for coherent responses.
- **Few-shot examples**: Enhanced query accuracy by passing relevant exaples in context.
- **GPT-4 Integration**: Leverage LLM to generate query and return reults in natural language.

## Technologies Used

- **LangChain**: Framework for interacting with LLM and quering database.
- **OpenAI Embeddings**: Generates vector representations of text for similarity search.
- **GPT-4o**: Large language model for generating responses.
- **Postgres DB**: Database on which we query and retrieve results.

## Folder Structure

```plaintext
├── Code
│   ├── app.py
│   ├── DatabaseActions.py
│   ├── LangchainAction.py
│   ├── main.py
│   ├── Testbed.py
│   ├── Hospital_Relational_Model.csv
├── Database Schema Files
│   ├──BCH.pdf
├── Langflow_UI
│   ├── RAG SQL Assistant.json
├── requirements.txt
```
# Description 

- **app.py** - This file contains the Streamlit frontend application.
- **DatabaseActions.py** - This file manages database-related actions, including connecting to and querying the database.
- **LangchainAction.py** - This file is responsible for handling language model actions through Langchain. It defines functions that process queries and use Langchain to generate responses based on the given data and question inpu
- **main.py** - This is the FastAPI backend entry point, where the API server is initialized and configured. 
- **Testbed.py** - A testing and development script used to try out individual components or functions in isolation. 
- **Hospital_Relational_Model.csv** - This CSV file contains a sample dataset description representing the relational model for a hospital.
- **BCH.pdf** - This PDF document contains a schema for the hospital database for the Langchain UI workflow.
- **RAG SQL Assistant.json** - A JSON file representing a Langflow UI workflow. This contains settings and configurations for the Langchain actions.
- **requirements.txt** - A text file listing all dependencies and libraries required to run the project, including specific versions.

## Prerequisites

- OpenAI API Key
- SQL Database 

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rag-sql-assistant.git
   cd rag-sql-assistant

2. **Install dependencies**
   ```bash
      pip install requirements.txt
   
3. **Create a .env file with the following information about your database and Open AI API key**

   DB_USER, DB_PASSWORD, DB_HOST, DB_NAME, OPENAI_API_KEY 
   
4. **Run FastAPI server and launch StreamLit app**
   uvicorn main:app --reload --port 8001
   streamlit run app.py

## License
- This project is licensed under the MIT License.

