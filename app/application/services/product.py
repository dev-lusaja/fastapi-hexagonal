from typing import List
from app.domain.use_cases.product import ProductUseCases
from app.domain.entities.product import ProductEntity
from app.domain.events.product import ProductCreatedEvent, ProductUpdatedEvent
from app.application.validators.product import ProductValidator
from app.domain.repositories.product import ProductRepository


class ProductService(ProductUseCases):

    __media_url = 'https://devlusaja.com/{}'

    def __init__(self, product_repository: ProductRepository,
                 product_created_event: ProductCreatedEvent,
                 product_updated_event: ProductUpdatedEvent
                 ):
        super().__init__(product_repository, product_created_event, product_updated_event)

    def products_catalog(self) -> List[ProductEntity]:
        products = self.product_repository.get_all()
        for product in products:
            product.image = self.__media_url.format(product.image)
        return products

    def product_detail(self, id: str) -> ProductEntity:
        product = self.product_repository.get_by_id(id)
        product.image = self.__media_url.format(product.image)
        return product

    def register_product(self, product: ProductEntity) -> ProductEntity:
        ProductValidator.validate_price_is_float(product.price)
        ProductValidator.validate_description_len(product.description)

        product = self.product_repository.add(product)
        product.image = self.__media_url.format(product.image)

        self.product_created_event.send(product)

        return product

    def update_product(self, product: ProductEntity) -> ProductEntity:
        ProductValidator.validate_price_is_float(product.price)
        ProductValidator.validate_description_len(product.description)

        product = self.product_repository.update(product)
        product.image = self.__media_url.format(product.image)

        self.product_updated_event.send(product)

        return product
