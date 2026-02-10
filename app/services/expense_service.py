from repositories import expense_repo

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