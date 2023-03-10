import uuid
from app.domain.exceptions import PriceIsLessThanOrEqualToZero, StockIsLessThanOrEqualToZero


class ProductEntity:

    def __init__(self, uid: str, name: str, description: str, price: float, stock: int, image: str):
        self.__validate_price(price)
        self.__validate_stock(stock)

        self.id = uid
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock
        self.image = image

    @staticmethod
    def __validate_price(price: float):
        if price <= 0:
            raise PriceIsLessThanOrEqualToZero

    @staticmethod
    def __validate_stock(stock: int):
        if stock <= 0:
            raise StockIsLessThanOrEqualToZero

class ProductEntityFactory:

    @staticmethod
    def create(id: str|None, name: str, description: str, price: float, stock: int, image: str) -> ProductEntity:
        if id is None:
            id = uuid.uuid4().__str__()
        return ProductEntity(id, name, description, float(price), int(stock), image)
