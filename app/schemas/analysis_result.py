from pydantic import BaseModel

class AnalysisResult(BaseModel):
    is_repetitive: bool
    automation_potential: int  # low | medium | high
    justification: str