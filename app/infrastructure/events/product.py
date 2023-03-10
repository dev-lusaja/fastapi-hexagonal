from app.domain.entities.product import ProductEntity
from app.domain.events.product import ProductCreatedEvent, ProductUpdatedEvent


class ProductCreatedQueueEvent(ProductCreatedEvent):

    def send(self, product: ProductEntity):
        # TODO: Your code here
        return True

class ProductUpdatedQueueEvent(ProductUpdatedEvent):

    def send(self, product: ProductEntity):
        # TODO: Your code here
        return True
