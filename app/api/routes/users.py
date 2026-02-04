from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schema import UserResponse
from api.deps import get_db, require_role
from repositories.user_repo import get_all_users

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse])
def list_users(
    db: Session = Depends(get_db),
    user=Depends(require_role("Admin"))
):
    return get_all_users(db)
