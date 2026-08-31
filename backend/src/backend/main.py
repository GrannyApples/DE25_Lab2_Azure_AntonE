from fastapi import FastAPI

app = FastAPI(
    title="eClipseBoard API",
    description="Backend API serving solar eclipse data for eClipseBoard.",
)


@app.get("/")
def root():
    return {"status": "ok", "service": "eClipseBoard API"}


@app.get("/health")
def health():
    return {"status": "healthy"}