from langchain_community.llms import Ollama

llm = Ollama(model="phi3")

def ask_llm(prompt: str) -> str:
    response = llm.invoke(prompt)
    return response.strip()
