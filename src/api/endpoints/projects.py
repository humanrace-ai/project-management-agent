from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...database import get_db
from ...schemas.project import ProjectCreate, Project, ProjectUpdate
from ...crud.project import create_project, get_project, update_project, delete_project, get_projects
from ...utils.github_cli import create_github_project, update_github_project, delete_github_project

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

@router.put("/{project_id}", response_model=Project)
async def update_project_endpoint(project_id: int, project: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    update_github_project(db_project.github_id, project.name, project.description)
    updated_project = await update_project(db, project_id, project)
    return updated_project

@router.delete("/{project_id}", response_model=dict)
async def delete_project_endpoint(project_id: int, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    delete_github_project(db_project.github_id)
    await delete_project(db, project_id)
    return {"message": "Project deleted successfully"}

@router.get("/", response_model=List[Project])
async def list_projects(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    projects = await get_projects(db, skip=skip, limit=limit)
    return projects

@router.get("/{project_id}/report")
async def generate_project_report(project_id: int, db: AsyncSession = Depends(get_db)):
    # Implement project report generation
    pass

@router.get("/{project_id}/burndown")
async def generate_burndown_chart(project_id: int, db: AsyncSession = Depends(get_db)):
    # Implement burndown chart data generation
    pass
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...database import get_db
from ...schemas.project import ProjectCreate, Project, ProjectUpdate
from ...crud.project import create_project, get_project, update_project, delete_project, get_projects
from ...utils.github_cli import create_github_project, update_github_project, delete_github_project

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

@router.put("/{project_id}", response_model=Project)
async def update_project_endpoint(project_id: int, project: ProjectUpdate, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    update_github_project(db_project.github_id, project.name, project.description)
    updated_project = await update_project(db, project_id, project)
    return updated_project

@router.delete("/{project_id}", response_model=dict)
async def delete_project_endpoint(project_id: int, db: AsyncSession = Depends(get_db)):
    db_project = await get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    
    delete_github_project(db_project.github_id)
    await delete_project(db, project_id)
    return {"message": "Project deleted successfully"}

@router.get("/", response_model=List[Project])
async def list_projects(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    projects = await get_projects(db, skip=skip, limit=limit)
    return projects
