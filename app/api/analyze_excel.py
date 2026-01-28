from fastapi import APIRouter, UploadFile, File
import pandas as pd
from app.services.llm_service import LLMService
from app.schemas.excel_analysis import ExcelAnalysisRequest
from app.core.config import OPENAI_API_KEY

router = APIRouter()

llm_service = LLMService(api_key=OPENAI_API_KEY)

@router.post("/analyze/excel", response_model=ExcelAnalysisRequest)
def analyze_excel(file: UploadFile = File(...)):

    df = pd.read_excel(file.file)

    results = []

    for _, row in df.iterrows():
        analysis = llm_service.analyze_text(row["process_description"])
        results.append(analysis)

    return ExcelAnalysisRequest(
        total_rows=len(results),
        results=results
    )