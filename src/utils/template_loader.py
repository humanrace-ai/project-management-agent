import toml
from pathlib import Path

def load_templates(templates_dir: str = "templates") -> dict[str, dict]:
    templates = {}
    for template_file in Path(templates_dir).glob("*.toml"):
        template_name = template_file.stem
        with open(template_file, "r") as f:
            templates[template_name] = toml.load(f)
    return templates
