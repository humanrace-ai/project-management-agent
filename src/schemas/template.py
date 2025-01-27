from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Dict, Any

class TemplateBase(BaseModel):
    name: str
    content: Dict[str, Any]

class TemplateCreate(TemplateBase):
    pass

class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[Dict[str, Any]] = None

class Template(TemplateBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True
