from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class IssueBase(BaseModel):
    title: str
    body: str
    status: str
    project_id: int

class IssueCreate(IssueBase):
    pass

class IssueUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    status: Optional[str] = None

class Issue(IssueBase):
    id: int
    github_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
