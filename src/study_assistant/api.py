from fastapi import FastAPI

app = FastAPI(title="Study Assistant")


@app.get("/health")
def health() -> dict[str, str]:
    """Simple check that the API is running."""
    return {"status": "ok"}