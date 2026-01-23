from fastapi import APIRouter
from app.schemas.analyse import AnalyzeRequest, AnalyzeResponse

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(request:AnalyzeRequest):
    return AnalyzeResponse(
        received_text=request.text,
        length=len(request.text),
        source=request.source
    )