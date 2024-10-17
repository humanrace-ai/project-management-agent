from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from typing import List

from ..models.template import Template
from ..schemas.template import TemplateCreate, TemplateUpdate

async def create_template(db: AsyncSession, template: TemplateCreate):
    db_template = Template(**template.dict())
    db.add(db_template)
    await db.commit()
    await db.refresh(db_template)
    return db_template

async def get_template(db: AsyncSession, template_id: int):
    result = await db.execute(select(Template).filter(Template.id == template_id))
    return result.scalars().first()

async def update_template(db: AsyncSession, template_id: int, template: TemplateUpdate):
    await db.execute(
        update(Template)
        .where(Template.id == template_id)
        .values(**template.dict(exclude_unset=True))
    )
    await db.commit()
    return await get_template(db, template_id)

async def delete_template(db: AsyncSession, template_id: int):
    await db.execute(delete(Template).where(Template.id == template_id))
    await db.commit()

async def get_templates(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Template]:
    result = await db.execute(select(Template).offset(skip).limit(limit))
    return result.scalars().all()
