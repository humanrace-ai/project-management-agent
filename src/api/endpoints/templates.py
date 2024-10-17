from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ...database import get_db
from ...schemas.template import TemplateCreate, Template, TemplateUpdate
from ...crud.template import create_template, get_template, update_template, delete_template
from ...utils.template_loader import load_templates_to_db, get_all_templates, apply_template_to_issue

router = APIRouter()

@router.on_event("startup")
async def startup_event():
    async with AsyncSession(get_db()) as db:
        await load_templates_to_db(db)

@router.get("/", response_model=List[Template])
async def list_templates(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    templates = await get_all_templates(db, skip=skip, limit=limit)
    return templates

@router.post("/", response_model=Template)
async def create_template_endpoint(template: TemplateCreate, db: AsyncSession = Depends(get_db)):
    db_template = await create_template(db, template)
    return db_template

@router.get("/{template_id}", response_model=Template)
async def read_template(template_id: int, db: AsyncSession = Depends(get_db)):
    db_template = await get_template(db, template_id)
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    return db_template

@router.put("/{template_id}", response_model=Template)
async def update_template_endpoint(template_id: int, template: TemplateUpdate, db: AsyncSession = Depends(get_db)):
    db_template = await get_template(db, template_id)
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    
    updated_template = await update_template(db, template_id, template)
    return updated_template

@router.delete("/{template_id}", response_model=dict)
async def delete_template_endpoint(template_id: int, db: AsyncSession = Depends(get_db)):
    db_template = await get_template(db, template_id)
    if db_template is None:
        raise HTTPException(status_code=404, detail="Template not found")
    
    await delete_template(db, template_id)
    return {"message": "Template deleted successfully"}

@router.post("/issues/{issue_id}/apply-template", response_model=dict)
async def apply_template_to_issue_endpoint(issue_id: int, template_id: int, db: AsyncSession = Depends(get_db)):
    result = await apply_template_to_issue(db, issue_id, template_id)
    if result:
        return {"message": "Template applied successfully"}
    else:
        raise HTTPException(status_code=400, detail="Failed to apply template")
