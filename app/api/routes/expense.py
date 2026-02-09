from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schema import ExpenseCreate
from repositories.expense_repo import get_expenses_by_user
from api.deps import get_current_user, get_db, require_role
from services.expense_service import create_user_expense, approve_expense, reject_expense

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/create")
def create_expense_api(expense: ExpenseCreate ,db: Session = Depends(get_db), user = Depends(get_current_user)):
    return create_user_expense(db, user.id, expense.dict())

@router.get("/list")
def list_expenses(db: Session = Depends(get_db), user = Depends(get_current_user)):
    return get_expenses_by_user(db, user.id)

@router.post("/{expense_id}/approve")
def approve_expense_api(expense_id: int, db: Session = Depends(get_db), user = Depends(require_role("Admin"))):
    return approve_expense(db, expense_id)

@router.post("/{expense_id}/reject")
def reject_expense_api(expense_id: int, db: Session = Depends(get_db), user = Depends(require_role("Admin"))):
    return reject_expense(db, expense_id)