from pydantic import BaseModel
from typing import List
from app.schemas.analysis_result import AnalysisResult


class ExcelAnalysisRequest(BaseModel):
    total_rows: int
    results: List[AnalysisResult]
