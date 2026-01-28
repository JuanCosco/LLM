from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
""" Imports Internos """
from app.api import health, analyze, analyze_excel

app = FastAPI( title= "My First API", version= "0.1.0")

app.mount("/static",StaticFiles(directory="frontend/static"), name="static")
templates = Jinja2Templates(directory="frontend/templates")

@app.get("/ui")
def ui(request: Request):
    return templates.TemplateResponse(
        "index.html", 
        {"request": request}
    )

app.include_router(health.router)
app.include_router(analyze.router)
app.include_router(analyze_excel.router)