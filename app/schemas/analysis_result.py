from pydantic import BaseModel

class AnalysisResult(BaseModel):
    is_repetitive: bool
    automation_potential: str  # low | medium | high
    justification: str