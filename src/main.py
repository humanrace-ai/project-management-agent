from fastapi import FastAPI
from .database import engine, Base
from .config import Settings
from .api.endpoints import projects, issues, templates
from .utils.template_loader import load_templates_to_db
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(title="AI Hacker League Project Management System")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    async with AsyncSession(engine) as db:
        await load_templates_to_db(db)

app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(issues.router, prefix="/issues", tags=["issues"])
app.include_router(templates.router, prefix="/templates", tags=["templates"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Hacker League Project Management System"}
