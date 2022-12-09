
##### Criar Virtual Env Local

```sh
Set-ExecutionPolicy AllSigned

python -m pip install virtualenv

python -m venv venv

pip install --upgrade pip

.\venv\scripts\activate

** criar o requirements.txt
pip freeze > requirements.txt

##### Instalar Requirements

pip install -r requirements.txt


** Rodar o projeto
uvicorn main:app
toda alteração precisar parar e roda novamente
uvicorn main:app --reload   #faz com que seja lido toda alteração salva
Ou fazer a configuração ...
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000,
                log_level="info", reload=True)

* Para compartilha na rede host="0.0.0.0"
if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,
                log_level="info", reload=True)


** para um ambiente de produção rodar. tem quer ser no Linux
pip install gunicorn  
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker 
-w 4 , quantidades servidores que vão rodar 
-k , classe que será execultada. uvicorn.workers.UvicornWorker  ...classe de alto desempenho


** Documentação do FastAPI 
http://127.0.0.1:8000/docs#/
http://127.0.0.1:8000/redoc