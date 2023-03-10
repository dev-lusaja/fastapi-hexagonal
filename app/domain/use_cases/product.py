from abc import ABC, abstractmethod
from typing import List
from app.domain.entities.product import ProductEntity
from app.domain.events.product import ProductCreatedEvent, ProductUpdatedEvent
from app.domain.repositories.product import ProductRepository


class ProductUseCases(ABC):

    @abstractmethod
    def __init__(self, product_repository: ProductRepository,
                 product_created_event: ProductCreatedEvent,
                 product_updated_event: ProductUpdatedEvent
                 ):
        self.product_repository = product_repository
        self.product_created_event = product_created_event
        self.product_updated_event = product_updated_event

    @abstractmethod
    def products_catalog(self) -> List[ProductEntity]:
        raise NotImplemented

    @abstractmethod
    def product_detail(self, id: str) -> ProductEntity:
        raise NotImplemented

    @abstractmethod
    def register_product(self, product: ProductEntity) -> ProductEntity:
        raise NotImplemented

    @abstractmethod
    def update_product(self, product: ProductEntity) -> ProductEntity:
        raise NotImplemented
