from db.models import Expense
from core.response import success_response

def create_expense(db, expense_data):
    expense = Expense(**expense_data)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return success_response(data=expense, message="Expense created successfully")
    # return expense

def get_expenses_by_user(db, user_id):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

def get_expense_by_id(db, expense_id):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def update_expense_status(db, expense, status):
    expense.status = status
    db.commit()
    db.refresh(expense)
    return success_response(data=expense, message="Expense Status Updated")
    # return expense

def get_filtered_expenses(db, user_id, status=None, category=None, skip=0, limit=10):
    query = db.query(Expense).filter(Expense.user_id == user_id)
    if status:
        query = query.filter(Expense.status == status)
    
    if category:
        query = query.filter(Expense.category == category)

    return query.offset(skip).limit(limit).all()