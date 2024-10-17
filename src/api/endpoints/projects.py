from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ...database import get_db
from ...schemas.project import ProjectCreate, Project
from ...crud.project import create_project, get_project
from ...utils.github_cli import create_github_project

router = APIRouter()

@router.post("/", response_model=Project)
async def create_project_endpoint(project: ProjectCreate, db: AsyncSession = Depends(get_db)):
    github_project = create_github_project(project.name, project.description)
    db_project = await create_project(db, project)
    db_project.github_id = github_project["id"]
    await db.commit()
    return db_project

@router.get("/{project_id}", response_model=Project)
async def read_project(project_id: int, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.get("/{project_id}/report")
async def generate_project_report(project_id: int, db: AsyncSession = Depends(get_db)):
    # Implement project report generation
    pass

@router.get("/{project_id}/burndown")
async def generate_burndown_chart(project_id: int, db: AsyncSession = Depends(get_db)):
    # Implement burndown chart data generation
    pass

# Implement other project endpoints (update, delete, list)
