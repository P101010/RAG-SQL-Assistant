# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from LangchainAction import LangchainActions
import os

app = FastAPI()

# Initialize LangchainActions with environment variables for database credentials
langchain = LangchainActions(user=os.getenv('DB_USER'), host=os.getenv('DB_HOST'), password=os.getenv('DB_PASSWORD'), name=os.getenv('DB_NAME'), file_name = 'Hospital_Relational_Model.csv', dbType='Postgres')

# Define a model for the message data
class Message(BaseModel):
    user: str
    message: str

# Endpoint to receive messages and process responses
@app.post("/chat/")
async def chat(message: Message):
    try:
        response = langchain.answer_query(message.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the FastAPI server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
