AGENTIC AI BACKEND SYSTEM
  A Python backend that demonstrates an agent-based AI workflow.
  The system understands user queries, selects the right agent, and responds using APIs, documents, or a database.

FEATURES: 
  - Weather queries using OpenWeather API
  - Document Q&A from uploaded PDFs with web fallback
  - Meeting scheduling based on weather and database logic
  - Natural language database queries
  - Hybrid routing (rules + LLM)

TECHSTACK:
 FastAPI, PgSQL, OpenAPIs

TO RUN:
  uvicorn app.main:app --reload

Docs:
  http://127.0.0.1:8000/docs

EXAMPLE QUERY:
{ "query": "Verify tomorrow’s weather and schedule a meeting in Chennai" }
