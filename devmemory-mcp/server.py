from fastapi import FastAPI
from pydantic import BaseModel

from memory.memory_manager import store_memory, query_memory
from sessions.session_summarizer import summarize_session
from context.context_builder import build_context, write_claude_md

app = FastAPI()


class MemoryInput(BaseModel):

    type: str
    content: str
    file_path: str | None = None
    function_name: str | None = None


@app.post("/store_memory")
def add_memory(data: MemoryInput):

    return store_memory(
        data.type,
        data.content,
        data.file_path,
        data.function_name
    )


@app.get("/search_memory")
def search(query: str):

    return query_memory(query)


class SessionInput(BaseModel):

    notes: str


@app.post("/summarize_session")
def summarize(data: SessionInput):

    return summarize_session(data.notes)


@app.get("/build_context")
def context(query: str):

    context = build_context(query)

    write_claude_md(context)

    return {"context": context}