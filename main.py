from fastapi import FastAPI
from routes import auth, book

app = FastAPI()

app.include_router(auth.router)
app.include_router(book.router)

@app.get("/")
def root():
    return {"message": "API is running"}
