from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated

from sqlalchemy import insert
from app.schemas import CreateProduct

from slugify import slugify
from sqlalchemy import select, update

router_p = APIRouter(prefix='/products', tags=['products'])

from app.models.products import Product
from app.models.category import Category


@router_p.get('/')
async def all_products(db: Annotated[Session, Depends(get_db)]):
    products = db.scalars(select(Product).where(Product.is_active == True, Product.stock > 0)).all()
    if products is None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no products'
        )
    return products


@router_p.post('/create')
async def create_product(db: Annotated[Session, Depends(get_db)], create_product: CreateProduct):
    db.execute(insert(Product).values(name=create_product.name,
                                      description=create_product.description,
                                      price=create_product.price,
                                      image_url=create_product.image_url,
                                      stock=create_product.stock,
                                      category_id=create_product.category,
                                      rating=0.0,
                                      slug=slugify(create_product.name)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router_p.get('/{category_slug}')
async def product_by_category(db: Annotated[Session, Depends(get_db)], category_slug: str):
    slugged_name = slugify(category_slug)
    category = db.scalar(select(Category).where(Category.slug == slugged_name))
    print(category.slug)
    if category is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Category not found'
        )
    subcategories = db.scalars(select(Category).where(Category.parent_id == category.id)).all()
    categories_and_subcategories = [category.id] + [i.id for i in subcategories]
    products_category = db.scalars(
        select(Product).where(Product.category_id.in_(categories_and_subcategories), Product.is_active == True,
                              Product.stock > 0)).all()
    return products_category


@router_p.get('/detail/{product_slug}')
async def product_detail(db: Annotated[Session, Depends(get_db)], product_slug: str):
    product = db.scalar(
        select(Product).where(Product.slug == product_slug, Product.is_active == True, Product.stock > 0))
    if not product:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There are no products'
        )
    return product


@router_p.put('/detail/{product_slug}')
async def update_product(db: Annotated[Session, Depends(get_db)], product_slug: str, update_product_model: CreateProduct):
    product_update = db.scalar(select(Product).where(Product.slug == product_slug))
    if product_update in None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )

    db.execute(update(Product).where(Product.slug == product_slug).values(name=update_product_model.name,
                                                                          descripyion=update_product_model.description,
                                                                          price=update_product_model.price,
                                                                          image_url=update_product_model.image_url,
                                                                          stock=update_product_model.stock,
                                                                          category_id=update_product_model.category,
                                                                          slug=slugify(update_product_model.name)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product update is successful'
    }


@router_p.delete('/delete')
async def delete_product(db: Annotated[Session, Depends(get_db)], product_id: int):
    product_delete = db.scalar(select(Product).where(Product.id == product_id))
    if product_delete is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='There is no product found'
        )
    db.execute(update(Product).where(Product.id == product_id).values(is_active=True))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Product delete is successful'
    }

