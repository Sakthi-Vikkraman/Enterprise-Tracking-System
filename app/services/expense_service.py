from repositories import expense_repo

def create_user_expense(db, user_id, expense_data):
    expense_data["user_id"] = user_id
    return expense_repo.create_expense(db, expense_data)