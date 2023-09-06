from fastapi import FastAPI
from routes.routes import routes as allRoutes

app = FastAPI()


@app.get(
    '/',
    tags=["Health Check"],
    summary="Rota default onde podemos verificar a saude da aplicação"
)
def healthCheck():
    return "Rodando"


app.include_router(allRoutes)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run('main:app', port=3334, reload=True)
