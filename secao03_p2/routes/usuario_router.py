from fastapi import APIRouter

router = APIRouter()


@router.get(path='/api/v1/usuarios')
async def get_usuarios():
    return {"info": "todos os usuarios"}