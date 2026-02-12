from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.orm import Session

from schema import ExpenseCreate
from repositories.expense_repo import get_expenses_by_user
from api.deps import get_current_user, get_db, require_role
from services.expense_service import create_user_expense, approve_expense, reject_expense, get_user_expense_service, upload_expenses_service

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

@router.get("/filter")
def filtered_expense(status: str = None, category: str = None, skip: int =0, limit: int = 10, db:Session = Depends(get_db), user = Depends(get_current_user)):
    return get_user_expense_service(db, user.id, status, category, skip, limit)

@router.post("/upload")
async def upload_expenses(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return await upload_expenses_service(file, db, current_user)