from repositories import expense_repo
from fastapi import HTTPException
from db.models import Expense
import json

def create_user_expense(db, user_id, expense_data):
    expense_data["user_id"] = user_id
    return expense_repo.create_expense(db, expense_data)

def approve_expense(db, expense_id):
    expense = expense_repo.get_expense_by_id(db, expense_id)
    if not expense:
        raise Exception("Expense not found")
    
    if(expense.status != "PENDING"):
        raise Exception("Only pending expenses can be approved")

    return expense_repo.update_expense_status(db, expense, "APPROVED")

def reject_expense(db, expense_id):
    expense = expense_repo.get_expense_by_id(db, expense_id)
    if not expense:
        raise Exception("Expense not found")
    
    if(expense.status != "PENDING"):
        raise Exception("Only pending expenses can be rejected")

    return expense_repo.update_expense_status(db, expense, "REJECTED")

def get_user_expense_service(db, user_id, status=None, category=None, skip=0, limit=10):
    return expense_repo.get_filtered_expenses(db, user_id, status, category, skip, limit)

async def upload_expenses_service(file, db, current_user):
    try:
        # Read file
        contents = await file.read()

        # Convert JSON → Python list
        expenses_data = json.loads(contents)

        if not isinstance(expenses_data, list):
            raise HTTPException(400, "JSON must be an array of expenses")

        expense_objects = []

        for item in expenses_data:
            expense = Expense(
                user_id=current_user.id,
                amount=item["amount"],
                category=item["category"],
                description=item.get("description", "")
            )
            expense_objects.append(expense)

        db.bulk_save_objects(expense_objects)
        db.commit()

        return {
            "message": f"{len(expense_objects)} expenses uploaded successfully"
        }

    except Exception as e:
        raise HTTPException(500, str(e))