from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

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

# Implement other CRUD operations (update, delete, list) for Project
