from fastapi import FastAPI

app = FastAPI(title="LeaseLens AI API")


@app.get("/")
async def root():
    return {"message": "Welcome to LeaseLens AI API"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
