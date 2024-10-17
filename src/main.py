from fastapi import FastAPI
from .api.endpoints import projects, issues, templates
from .database import engine, Base

app = FastAPI(title="AI Hacker League Project Management System")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(issues.router, prefix="/issues", tags=["issues"])
app.include_router(templates.router, prefix="/templates", tags=["templates"])

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Hacker League Project Management System"}
