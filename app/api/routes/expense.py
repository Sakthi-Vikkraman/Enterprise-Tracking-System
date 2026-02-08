from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import ExpenseCreate
from repositories.expense_repo import get_expenses_by_user
from api.deps import get_current_user, get_db
from services.expense_service import create_user_expense

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/create")
def create_expense_api(expense: ExpenseCreate ,db: Session = Depends(get_db), user = Depends(get_current_user)):
    return create_user_expense(db, user.id, expense.dict())

@router.get("/list")
def list_expenses(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_expenses_by_user(db, user.id)