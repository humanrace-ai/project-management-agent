from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List

from ..models.issue import Issue
from ..schemas.issue import IssueCreate, IssueUpdate

async def create_issue(db: AsyncSession, issue: IssueCreate):
    db_issue = Issue(**issue.dict())
    db.add(db_issue)
    await db.commit()
    await db.refresh(db_issue)
    return db_issue

async def get_issue(db: AsyncSession, issue_id: int):
    result = await db.execute(select(Issue).filter(Issue.id == issue_id))
    return result.scalars().first()

async def update_issue(db: AsyncSession, issue_id: int, issue: IssueUpdate):
    await db.execute(
        update(Issue)
        .where(Issue.id == issue_id)
        .values(**issue.dict(exclude_unset=True))
    )
    await db.commit()
    return await get_issue(db, issue_id)

async def delete_issue(db: AsyncSession, issue_id: int):
    await db.execute(delete(Issue).where(Issue.id == issue_id))
    await db.commit()

async def get_issues(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Issue]:
    result = await db.execute(select(Issue).offset(skip).limit(limit))
    return result.scalars().all()
