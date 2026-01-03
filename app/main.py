from fastapi import FastAPI, UploadFile, File
from app.agents import weather_agent, meeting_agent, document_agent, db_agent
from app.agents.router_llm import route_query
from app.tools.pdf_loader import load_pdf_text
import os
from fastapi.responses import HTMLResponse
app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h1>Agentic AI Workflow Chatbot</h1>
    <ul>
        <li>Weather Agent</li>
        <li>Document Agent</li>
        <li>Meeting Agent</li>
        <li>DB Agent</li>
    </ul>
    <p><strong>API is running successfully</strong></p>
    """

@app.post("/ask")
def ask(query: str):
    decision = route_query(query)

    if decision == "weather":
        return {"response": weather_agent.handle(query)}

    elif decision == "meeting":
        return {"response": meeting_agent.handle(query)}

    elif decision == "document":
        return {"response": document_agent.handle(query)}

    elif decision == "db":
        return {"response": db_agent.handle(query)}

    return {"response": "Sorry, I did not understand your request."}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    os.makedirs("docs", exist_ok=True)

    file_path = f"docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    lines = load_pdf_text(file_path)
    document_agent.set_document(lines)

    return {"message": "Document uploaded successfully"}
