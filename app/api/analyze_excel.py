from fastapi import APIRouter, UploadFile, File
from app.services.llm_service import LLMService
from app.schemas.excel_analysis import ExcelAnalysisRequest
from app.core.config import OPENAI_API_KEY

import pandas as pd
import asyncio

router = APIRouter()

llm_service = LLMService(api_key=OPENAI_API_KEY)

@router.post("/analyze/excel", response_model=ExcelAnalysisRequest)
async def analyze_excel(file: UploadFile = File(...)):

    df = pd.read_excel(file.file)

    tasks = [
        llm_service.analyze_process(row["process_description"])
        for _, row in df.iterrows()
    ]
            
    raw_results = await asyncio.gather(*tasks)

    results = raw_results

    return ExcelAnalysisRequest(
        total_rows=len(results),
        results=results
    )