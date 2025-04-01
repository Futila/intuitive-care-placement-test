from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router

app = FastAPI(title="Teste de API", description="API simples para nivelamento")
# Configuraração do CORS para permitir requisições do Vue.js
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Permite requisições do Vue.js rodando no Vite
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Inclui as rotas do arquivo routes.py
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000,)
