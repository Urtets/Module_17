from fastapi import FastAPI
from routers import category, products

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My e-commerce app"}


app.include_router(category.router)
