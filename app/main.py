from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from db.database import Base, engine
from api.routes import auth, users, expense

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(expense.router)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )