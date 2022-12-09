from pickle import NONE
from typing import Optional
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from fastapi import Response
from fastapi import Path
from fastapi import Query
from fastapi import Header

from models import Curso

app = FastAPI()


cursos: list[Curso] = []

curso1 = Curso(id=1, titulo="Programação para Leigos", aulas=112, horas=58)
curso2 = Curso(id=2, titulo="Programação em python", aulas=60, horas=41)

cursos.append(curso1)
cursos.append(curso2)


@app.get('/cursos')
async def get_cursos():
    return cursos


@app.get('/cursos/{curso_id}')
async def get_curso(curso_id: int = Path(default=None,
                                         title='ID do curso',
                                         description="Deve ser entre 1 e 2",
                                         gt=0, 
                                         lt=3
                                         )):
    try:
        curso = next(x for x in cursos if x.id == curso_id)
        return curso
    except IndexError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail="Curso não encontrado.")
    


@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def post_curso(curso: Curso):
    if curso.id not in cursos:
        curso.id = len(cursos) + 1
        cursos.append(curso)
        return curso
    else:
        HTTPException(status_code=status.HTTP_409_CONFLICT, 
                      detail=f"Já existe um curso com o ID {curso.id}.")


@app.put('/cursos/{curso_id}')
async def put_curso(curso_id:int, curso:Curso):
    curso_existe = False
    for i, item in enumerate(cursos):
        if item.id == curso_id:
            cursos[i] = curso
            curso_existe = True
            break
    
    if not curso_existe:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Não existe um curso com o Id {curso_id}")
        
    return curso


@app.delete('/cursos/{curso_id}')
async def delete_curso(curso_id:int):
    curso_existe = False
    for i, item in enumerate(cursos):
        if item.id == curso_id:
            del cursos[i]
            curso_existe = True
            break
    
    if curso_existe:
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Não existe um curso com o Id {curso_id}")
        

@app.get('/calculadora')
async def calculadora(a: int = Query(default=None, gt=5), 
                      b:int = Query(default=None, gt=10),
                      x_geek: str = Header(default=None),
                      c: Optional[int]= None):
    soma = a + b
    if c:
        soma += c
    return {"resultado": soma, "x_geek":x_geek}
        

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, debug=True, reload=True)