from typing import List
from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends
from app.domain.entities.product import ProductEntity, ProductEntityFactory
from app.infrastructure.container import Container
from app.application.services.product import ProductService
from app.infrastructure.schemas.product import ProductOutput, ProductInput

router = APIRouter(
    prefix='/products',
    tags=['products']
)

@router.get('/', response_model=List[ProductOutput])
@inject
def get_catalog(product_services: ProductService = Depends(Provide[Container.product_services])) -> List[dict]:
    response: List[ProductEntity] = product_services.products_catalog()
    return [product_entity.__dict__ for product_entity in response]

@router.get('/{id}', response_model=ProductOutput)
@inject
def get_description(id: str, product_services: ProductService = Depends(Provide[Container.product_services])) -> dict:
    response: ProductEntity = product_services.product_detail(id)
    return response.__dict__

@router.post('/', response_model=ProductOutput)
@inject
def register_product(
        product: ProductInput,
        product_factory: ProductEntityFactory = Depends(Provide[Container.product_factory]),
        product_services: ProductService = Depends(Provide[Container.product_services])
) -> dict:
    name, description, price, stock, image = product.__dict__.values()
    product_entity: ProductEntity = product_factory.create(None, name, description, price, stock, image)
    response: ProductEntity = product_services.register_product(product_entity)
    return response.__dict__

@router.put('/{id}', response_model=ProductOutput)
@inject
def update_product(
        id: str,
        product: ProductInput,
        product_factory: ProductEntityFactory = Depends(Provide[Container.product_factory]),
        product_services: ProductService = Depends(Provide[Container.product_services])
) -> dict:
    name, description, price, stock, image = product.__dict__.values()
    product_entity: ProductEntity = product_factory.create(id, name, description, price, stock, image)
    response: ProductEntity = product_services.update_product(product_entity)
    return response.__dict__
