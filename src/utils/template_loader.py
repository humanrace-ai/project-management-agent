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

def load_templates(templates_dir: str = "templates") -> dict[str, dict]:
    templates = {}
    for template_file in Path(templates_dir).glob("*.toml"):
        template_name = template_file.stem
        with open(template_file, "r") as f:
            templates[template_name] = toml.load(f)
    return templates
