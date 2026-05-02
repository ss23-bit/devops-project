import logging
from fastapi import FastAPI
from routes import router


# Log levels (from low → high), Default level is Warning (DEBUG < INFO < WARNING < ERROR < CRITICAL)
# logs can be collected (CloudWatch, ELK, etc.)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="DevOps Project API") 

app.include_router(router) 

@app.get("/")
def root():
    logging.info("Root endpoint called")
    return {"message": "API is running"}


