from fastapi import APIRouter, Depends
from api.deps import require_role

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.post("/approve/{expense_id}")
def approve_expense(
    expense_id: int,
    user=Depends(require_role("Manager"))
):
    return {"message": f"Expense {expense_id} approved"}
