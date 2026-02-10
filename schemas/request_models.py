from pydantic import BaseModel, Field
from typing import Literal


class SummarizeRequest(BaseModel):
    text: str = Field(..., min_length=10, max_length=20000)
    summary_type: Literal["concise", "detailed", "bullet_points"] = "concise"
    max_tokens: int = Field(default=200, ge=50, le=1000)
    temperature: float = Field(default=0.3, ge=0.0, le=1.0)
    top_p: float = Field(default=0.1, ge=0.0, le=1.0)