from fastapi import FastAPI
from app.api import health, analyze

app = FastAPI(
    title= "My First API",
    version= "0.1.0"
)

app.include_router(health.router)
app.include_router(analyze.router)