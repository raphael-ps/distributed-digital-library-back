from fastapi import FastAPI
from routes import auth, book
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

# Permitir chamadas do frontend
origins = [
    "*",  # ou "*" para liberar tudo (não recomendado em produção)
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # ou ["*"] para liberar todos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(book.router)

@app.get("/")
def root():
    return {"message": "API is running"}
