from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...database import get_db
from ...schemas.issue import IssueCreate, Issue, IssueUpdate
from ...crud.issue import create_issue, get_issue, update_issue, delete_issue, get_issues
from ...utils.github_cli import create_github_issue, update_github_issue, delete_github_issue

router = APIRouter()

@router.post("/", response_model=Issue)
async def create_issue_endpoint(issue: IssueCreate, db: AsyncSession = Depends(get_db)):
    github_issue = create_github_issue(issue.project_id, issue.title, issue.body)
    db_issue = await create_issue(db, issue)
    db_issue.github_id = github_issue["id"]
    await db.commit()
    return db_issue

@router.get("/{issue_id}", response_model=Issue)
async def read_issue(issue_id: int, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue

@router.put("/{issue_id}", response_model=Issue)
async def update_issue_endpoint(issue_id: int, issue: IssueUpdate, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    
    update_github_issue(db_issue.github_id, issue.title, issue.body, issue.status)
    updated_issue = await update_issue(db, issue_id, issue)
    return updated_issue

@router.delete("/{issue_id}", response_model=dict)
async def delete_issue_endpoint(issue_id: int, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    
    delete_github_issue(db_issue.github_id)
    await delete_issue(db, issue_id)
    return {"message": "Issue deleted successfully"}

@router.get("/", response_model=List[Issue])
async def list_issues(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    issues = await get_issues(db, skip=skip, limit=limit)
    return issues

@router.post("/{issue_id}/assign", response_model=Issue)
async def assign_issue(issue_id: int, assignee: str, db: AsyncSession = Depends(get_db)):
    # Implement issue assignment
    pass

@router.put("/{issue_id}/status", response_model=Issue)
async def change_issue_status(issue_id: int, status: str, db: AsyncSession = Depends(get_db)):
    # Implement issue status change
    pass
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...database import get_db
from ...schemas.issue import IssueCreate, Issue, IssueUpdate
from ...crud.issue import create_issue, get_issue, update_issue, delete_issue, get_issues
from ...utils.github_cli import create_github_issue, update_github_issue, delete_github_issue

router = APIRouter()

@router.post("/", response_model=Issue)
async def create_issue_endpoint(issue: IssueCreate, db: AsyncSession = Depends(get_db)):
    github_issue = create_github_issue(issue.project_id, issue.title, issue.body)
    db_issue = await create_issue(db, issue)
    db_issue.github_id = github_issue["id"]
    await db.commit()
    return db_issue

@router.get("/{issue_id}", response_model=Issue)
async def read_issue(issue_id: int, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    return db_issue

@router.put("/{issue_id}", response_model=Issue)
async def update_issue_endpoint(issue_id: int, issue: IssueUpdate, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    
    update_github_issue(db_issue.github_id, issue.title, issue.body, issue.status)
    updated_issue = await update_issue(db, issue_id, issue)
    return updated_issue

@router.delete("/{issue_id}", response_model=dict)
async def delete_issue_endpoint(issue_id: int, db: AsyncSession = Depends(get_db)):
    db_issue = await get_issue(db, issue_id)
    if db_issue is None:
        raise HTTPException(status_code=404, detail="Issue not found")
    
    delete_github_issue(db_issue.github_id)
    await delete_issue(db, issue_id)
    return {"message": "Issue deleted successfully"}

@router.get("/", response_model=List[Issue])
async def list_issues(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    issues = await get_issues(db, skip=skip, limit=limit)
    return issues

@router.post("/{issue_id}/assign", response_model=Issue)
async def assign_issue(issue_id: int, assignee: str, db: AsyncSession = Depends(get_db)):
    # Implement issue assignment
    pass

@router.put("/{issue_id}/status", response_model=Issue)
async def change_issue_status(issue_id: int, status: str, db: AsyncSession = Depends(get_db)):
    # Implement issue status change
    pass
