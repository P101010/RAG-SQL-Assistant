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

The **RAG SQL Assistant** is a powerful Retrieval-Augmented Generation (RAG) tool designed to help users generate queries to interact with SQL databases through natural language queries. By leveraging LangChain, OpenAI embeddings, GPT-4o, and Datastax Astra DB, this assistant provides context-aware interactions, translating user queries into actionable SQL commands and retrieving relevant information.

## Features

- **Natural Language Processing**: Interact with SQL databases using plain English queries.
- **Chat Memory**: Maintains context across interactions for coherent responses.
- **Vector-Based Retrieval**: Uses embeddings to store and search database information efficiently.
- **GPT-4 Integration**: Generates accurate, contextually appropriate responses.
- **Scalable Database Management**: Utilizes Datastax Astra DB for efficient vector storage and retrieval.

## Architecture

1. **User Interaction**: Users enter natural language queries.
2. **Embedding Generation**: Converts both the user query and database documents into embeddings using OpenAI.
3. **Vector Search**: Finds the most relevant information in vector space(closest distance).
4. **Prompt Construction**: Combines retrieved information with the user query to create a prompt.
5. **Response Generation**: Sends the prompt to GPT-4o for a meaningful response.
6. **Chat Memory**: Retains conversation context to handle follow-up queries effectively.

## Technologies Used

- **LangChain**: Framework for building applications with LLMs.
- **OpenAI Embeddings**: Generates vector representations of text for similarity search.
- **GPT-4o**: Large language model for generating responses.
- **Datastax Astra DB (Vector DB)**: Managed database optimized for vector storage and retrieval.

## Prerequisites

- Datastax Astra DB Account
- OpenAI API Key
- Astra DB Credentials: Secure connect bundle, Client ID, and Client Secret

## Usage

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rag-sql-assistant.git
   cd rag-sql-assistant

2. **Install and run Langchain**
   ```bash
   pip install Langchain
   run langchain
   
3. **Change schema file**
   
4. **Import RAG SQL Assistant.json file into Langchain and playaround**

## License
- This project is licensed under the MIT License.

