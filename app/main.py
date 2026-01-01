from fastapi import FastAPI

from app.agents import weather_agent, meeting_agent, document_agent, router_agent

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

    return {"response": "Sorry, I did not understand your request."}
