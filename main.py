from fastapi import FastAPI
from app.routers import category, products


# import sys
#
# print(sys.path)


app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "My e-commerce app"}


app.include_router(category.router_c)
app.include_router(products.router_p)
