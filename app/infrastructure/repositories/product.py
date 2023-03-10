from copy import copy
from typing import List
from app.domain.entities.product import ProductEntityFactory, ProductEntity
from app.domain.repositories.product import ProductRepository


class ProductInMemoryRepository(ProductRepository):

    products: List[dict] = [
        {'id': '3f996431-e90e-4d12-b2be-5614959c0202', 'name': 'milk', 'description': 'skimmed cows milk', 'price': 10.50, 'stock': 1, 'image': 'milk.jpg'},
        {'id': '3f996431-e90e-4d12-b2be-5614959c0201', 'name': 'meat', 'description': 'beef licence', 'price': 20.50, 'stock': 2, 'image': 'meat.jpg'}
    ]

    def get_all(self) -> List[ProductEntity]:
        return [ProductEntityFactory.create(**product) for product in self.products]

    def get_by_id(self, id: str) -> ProductEntity|None:
        try:
            product = next(filter(lambda p: p['id'] == id, self.products))
            return ProductEntityFactory.create(**product)
        except StopIteration:
            return None

    def add(self, product: ProductEntity) -> ProductEntity:
        self.products.append(copy(product.__dict__))
        return product

    def update(self, product: ProductEntity) -> ProductEntity:
        for key, value in enumerate(self.products):
            if value['id'] == product.id:
                self.products[key] = copy(product.__dict__)
        return product
