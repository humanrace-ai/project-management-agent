from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List

from ..models.project import Project
from ..schemas.project import ProjectCreate, ProjectUpdate

async def create_project(db: AsyncSession, project: ProjectCreate):
    db_project = Project(**project.dict())
    db.add(db_project)
    await db.commit()
    await db.refresh(db_project)
    return db_project

async def get_project(db: AsyncSession, project_id: int):
    result = await db.execute(select(Project).filter(Project.id == project_id))
    return result.scalars().first()

async def update_project(db: AsyncSession, project_id: int, project: ProjectUpdate):
    await db.execute(
        update(Project)
        .where(Project.id == project_id)
        .values(**project.dict(exclude_unset=True))
    )
    await db.commit()
    return await get_project(db, project_id)

async def delete_project(db: AsyncSession, project_id: int):
    await db.execute(delete(Project).where(Project.id == project_id))
    await db.commit()

async def get_projects(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Project]:
    result = await db.execute(select(Project).offset(skip).limit(limit))
    return result.scalars().all()
