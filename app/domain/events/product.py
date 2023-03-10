from abc import ABC, abstractmethod
from app.domain.entities.product import ProductEntity

class ProductCreatedEvent(ABC):

    @abstractmethod
    def send(self, product: ProductEntity) -> bool:
        raise NotImplemented

class ProductUpdatedEvent(ABC):

    @abstractmethod
    def send(self, product: ProductEntity) -> bool:
        raise NotImplemented
