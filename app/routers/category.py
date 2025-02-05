from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
# from app.backend.db_depends import get_db
from typing import Annotated

from app.models.category import *
# from app.models.products import *
from sqlalchemy import insert, select, update

# from app.models.category import Category
from app.schemas import CreateCategory

from slugify import slugify

router_c = APIRouter(prefix='/category', tags=["category"])

@router_c.post("/create")
async def create_category(db: Annotated[Session, Depends()], create_category: CreateCategory):
    # db.execute(insert(Category).values(name=create_category.name, parent_id=create_category.parent_id,
    #                                    slug=slugify(create_category.name)))
    # db.commit()
    # return {
    #     'status_code': status.HTTP_201_CREATED,
    #     'transaction': 'Successful'
    # }
    pass


@router_c.get('/all_categories')
async def get_all_categories(db: Annotated[Session, Depends()]):
    # categories = db.scalars(select(Category).where(Category.is_active == True)).all()
    # return categories
    pass


@router_c.put("/update_category")
async def update_category(db: Annotated[Session, Depends()], category_id: int,
                          update_category: CreateCategory):
    # category = db.scalar(select(Category).where(Category.id == category_id))
    # if category is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail='There is no category found')
    # db.execute(update(Category).where(Category.id == category_id).values(
    #     name=update_category.name,
    #     slug=slugify(update_category.name),
    #     parent_id=update_category.parent_id
    # ))
    # db.commit()
    # return {
    #     'status_code': status.HTTP_200_OK,
    #     'transaction': 'Category update is successful'
    # }
    pass

from sqlalchemy import update

@router_c.delete("/delete")
async def delete_category(db: Annotated[Session, Depends()], category_id: int):
    # category = db.scalar(select(Category).where(Category.id == category_id))
    # if category is None:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail='There is no category found'
    #     )
    # db.execute(update(Category).where(Category.id == category_id).values(is_active=False))
    # db.commit()
    # return {
    #     'status_code': status.HTTP_200_OK,
    #     'transaction': 'Category delete is successful'
    # }
    pass
