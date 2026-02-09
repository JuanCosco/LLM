from pydantic import BaseModel


class AnalyzeRequest(BaseModel):
    text: str
    source: str


class AnalyzeResponse(BaseModel):
    received_text: str
    length: int
    source: str
