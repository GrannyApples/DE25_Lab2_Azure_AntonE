from fastapi import FastAPI
from backend.data import load_eclipse, to_json_safe_records

app = FastAPI(
    title="eClipseBoard API",
    description="Backend API serving solar eclipse data for eClipseBoard.",
)

@app.get("/eclipses")
def get_eclipses(limit: int = 100):
    df = load_eclipse()
    return to_json_safe_records(df.head(limit))

@app.get("/")
def root():
    return {"status": "ok", "service": "eClipseBoard API"}


@app.get("/health")
def health():
    return {"status": "healthy"}