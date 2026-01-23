from fastapi import APIRouter
from app.schemas.analyse import AnalyzeRequest
from app.schemas.analysis_result import AnalysisResult
from app.services.llm_service import LLMService
from app.core.config import OPENAI_API_KEY

router = APIRouter()

llm_service = LLMService(api_key=OPENAI_API_KEY)

@router.post("/analyze", response_model=AnalysisResult)
def analyze(request:AnalyzeRequest):

    llm_result = llm_service.analyze_text(request.text)
    return llm_result