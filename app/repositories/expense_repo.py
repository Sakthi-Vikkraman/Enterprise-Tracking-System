from db.models import Expense

def create_expense(db, expense_data):
    expense = Expense(**expense_data)
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense

def get_expenses_by_user(db, user_id):
    return db.query(Expense).filter(Expense.user_id == user_id).all()

def get_expense_by_id(db, expense_id):
    return db.query(Expense).filter(Expense.id == expense_id).first()

def update_expense_status(db, expense, status):
    expense.status = status
    db.commit()
    db.refresh(expense)
    return expense