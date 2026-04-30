from fastapi import FastAPI
from routes import router

app = FastAPI(title="DevOps Project API") 

app.include_router(router) 

@app.get("/")
def root():
    return {"message": "API is running"}


