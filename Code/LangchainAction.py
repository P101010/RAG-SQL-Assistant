from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from operator import itemgetter
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.chains.openai_tools import create_extraction_chain_pydantic
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List
import pandas as pd
import os
import re


class LangchainActions:

   
    def __init__(self, user, host, password, name, dbType, file_name, model='gpt-4o'):
        os.environ["OPENAI_API_KEY"] = # Add your API key
        self.user = user
        self.host = host
        self.password = password
        self.name = name
        self.dbType = dbType
        self.model = model
        self.filename = file_name
       
    # Method to craete URI with relevant tables from schema 
    def createURI(self, dbType, tabelnames:list, rows=3):
        if dbType == 'MySQL':
            return SQLDatabase.from_uri(f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.name}", sample_rows_in_table_info = rows, include_tables = tabelnames)
        elif dbType == 'Postgres':
            return SQLDatabase.from_uri(f"postgresql+psycopg2://{self.user}:{self.password}@{self.host}/{self.name}", sample_rows_in_table_info = rows, include_tables = tabelnames)

    # Retrieve table description from pdf
    def get_table_details(self, filename):
        # Read the CSV file into a DataFrame
        table_description = pd.read_csv(filename)
        table_docs = []

        # Iterate over the DataFrame rows to create Document objects
        table_details = ""
        for index, row in table_description.iterrows():
            table_details = table_details + "Table Name:" + row['Table Name'].lower() + "\n" + "Table Description:" + row['Description'] + "\n\n"

        return table_details

    # Method to generate query, retrieve query result from database and return reult in a natural language
    def answer_query(self, question:str):
        llm = ChatOpenAI(model = self.model, temperature=0)

        # Retrieve relevant tables
        table_details = self.get_table_details(self.filename)
        table_details_prompt = f"""Return the names of ALL the SQL tables that MIGHT be relevant to the user question. \
        The tables are:

        {table_details}

        Remember to include ALL POTENTIALLY RELEVANT tables, even if you're not sure that they're needed."""

        class Table(BaseModel):
            """Table in SQL database."""

            name: str = Field(description="Name of table in SQL database.")

        def get_tables(tables: List[Table]) -> List[str]:
            tables  = [table.name for table in tables]
            return tables
        
        select_table = {"input": itemgetter("question")} | create_extraction_chain_pydantic(Table, llm, system_message=table_details_prompt) | get_tables
        tables = select_table.invoke({"question": question})
        
        # based on the retrieved tables genrate appropriate URI
        db = self.createURI(self.dbType, tables)

        # Genearte query
        generate_query = create_sql_query_chain(llm, db)

        # Excecute query
        execute_query = QuerySQLDataBaseTool(db = db)
        
        answer_prompt = PromptTemplate.from_template(
            """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

        Question: {question}
        SQL Query: {query}
        SQL Result: {result}
        Answer: """
        )

        # Chain to rephrase answer
        rephrase_answer = answer_prompt | llm | StrOutputParser()

        def stripper(query:str):
            # Adjust regex to capture content within ```sql and ```
            match = re.search(r"```sql\n(.*?)\n```", query, re.DOTALL)
            if match:
                return (match.group(1)).replace('SQLQuery:', '').strip()
            return None

        # Final chain to genrate and clean query followed by exceting thye query on the databse and rephrasing the answer
        chain = (
            RunnablePassthrough.assign(query=generate_query)
            .assign(clean_query=lambda x: stripper(x['query']))
            .assign(result=itemgetter("clean_query") | execute_query
            )
            | rephrase_answer
        )

        return chain.invoke({"question": question})

        
    
