import logging
from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from routes import router
from starlette.responses import Response

# Log levels (from low → high), Default level is Warning (DEBUG < INFO < WARNING < ERROR < CRITICAL)
# logs can be collected (CloudWatch, ELK, etc.)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = FastAPI(title="DevOps Project API") 

REQUEST_COUNT = Counter("app_requests_total", "total requests")

app.include_router(router) 

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    logging.info("Root endpoint called")
    return {"message": "API is running"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")


