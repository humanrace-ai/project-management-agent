from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Dict, Any
from pydantic import BaseModel

from ...database import get_db
from ...schemas.template import Template, TemplateCreate, TemplateUpdate
from ...crud.template import get_templates, create_template, get_template, update_template, delete_template
from ...utils.template_loader import list_available_templates, apply_template_to_issue

router = APIRouter()

class TemplateInfo(BaseModel):
    id: int
    name: str
    title: str
    fields: Dict[str, Dict[str, Any]]

@router.get("/available", response_model=List[str])
async def list_available_templates_endpoint():
    """
    List all available template names.
    """
    return list_available_templates()


@router.get("/", response_model=List[TemplateInfo])
async def list_templates(
    skip: int = 0, 
    limit: int = 100, 
    name: str = Query(None, description="Filter templates by name"),
    db: AsyncSession = Depends(get_db)
):
    templates = await get_templates(db, skip=skip, limit=limit)
    template_info_list = []
    for template in templates:
        if name and name.lower() not in template.name.lower():
            continue
        template_info = TemplateInfo(
            id=template.id,
            name=template.name,
            title=template.content.get("title", ""),
            fields=template.content.get("fields", {})
        )
        template_info_list.append(template_info)
    return template_info_list

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
