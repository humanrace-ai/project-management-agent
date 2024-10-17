import toml
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession

def load_templates(templates_dir: str = "templates") -> dict[str, dict]:
    templates = {}
    for template_file in Path(templates_dir).glob("*.toml"):
        template_name = template_file.stem
        with open(template_file, "r") as f:
            templates[template_name] = toml.load(f)
    return templates

async def apply_template_to_issue(db: AsyncSession, issue_id: int, template_id: int) -> bool:
    # Implement the logic to apply a template to an issue
    # This function should:
    # 1. Load the template
    # 2. Get the issue
    # 3. Apply the template to the issue
    # 4. Update the issue in the database
    # 5. Return True if successful, False otherwise
    pass
import toml
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from ..models.template import Template
from ..schemas.template import TemplateCreate
from ..crud.template import create_template, get_templates
from typing import List

async def load_templates_to_db(db: AsyncSession, templates_dir: str = "templates") -> None:
    # First, get all existing template names
    existing_templates = {template.name for template in await get_templates(db)}

    for template_file in Path(templates_dir).glob("*.toml"):
        template_name = template_file.stem
        if template_name not in existing_templates:
            with open(template_file, "r") as f:
                template_content = toml.load(f)
                template_create = TemplateCreate(name=template_name, content=template_content)
                await create_template(db, template_create)

    await db.commit()

async def get_all_templates(db: AsyncSession, skip: int = 0, limit: int = 100) -> list[Template]:
    return await get_templates(db, skip=skip, limit=limit)

def list_available_templates(templates_dir: str = "templates") -> List[str]:
    """
    List all available template names in the templates directory.
    """
    return [template_file.stem for template_file in Path(templates_dir).glob("*.toml")]
