from fastapi import APIRouter



router = APIRouter(
    prefix="/user",
    tags=["User"],
)


@router.get("/")
def find_all():
   return 'oi meu chapa'
