from fastapi import FastAPI

from routes import cursos_router
from routes import usuario_router

app = FastAPI()

app.include_router(cursos_router.router, tags=['Cursos'])
app.include_router(usuario_router.router, tags=['Usuários'])


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)