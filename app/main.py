from fastapi import FastAPI

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
