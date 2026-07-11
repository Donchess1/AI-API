from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome, I am Stephen"}

@app.get("/status")
def read_status():
    return {
        "status": "healthy",
        "active_model": "Steph 001",
        "gpu_available": False
    }