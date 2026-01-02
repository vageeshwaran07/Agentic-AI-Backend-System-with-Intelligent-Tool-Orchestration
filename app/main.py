from fastapi import FastAPI, UploadFile, File
from .agents import weather_agent, meeting_agent, document_agent, router_agent, db_agent
from .tools.pdf_loader import load_pdf_text

app = FastAPI()


@app.post("/ask")
def ask(query: str):
    decision = router_agent.router(query)

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
    file_path = f"docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    lines = load_pdf_text(file_path)
    document_agent.set_document(lines)

    return {"message": "Document uploaded successfully"}