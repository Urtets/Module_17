from fastapi import FastAPI
# from routers import category, products
from routers.category import router_c
from routers.products import router_p

import sys

print(sys.path)


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My e-commerce app"}


app.include_router(router_c)
app.include_router(router_p)
