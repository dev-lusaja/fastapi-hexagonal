import pytest
from app.application.services.product import ProductService
from app.domain.entities.product import ProductEntity, ProductEntityFactory
from app.infrastructure.container import Container
from app.test import create_mock_product_repository
from app.test.data.product import expected_product_description


class TestProductService:

    """
    this fixture fulfills the function of dependency injection for all tests
    """
    @pytest.fixture(autouse=True)
    def injector(self):
        container = Container()
        with container.product_repository.override(create_mock_product_repository()):
            self.product_service: ProductService = container.product_services()
            self.product_factory: ProductEntityFactory = container.product_factory()

    def test_that_all_products_in_the_catalog_are_an_entity(self):
        catalog = self.product_service.products_catalog()
        for product in catalog:
            assert type(product) is ProductEntity

    def test_that_product_detail_is_an_entity(self):
        product = self.product_service.product_detail('mock_id')
        assert type(product) is ProductEntity

    def test_product_name_is_correct(self):
        product = self.product_service.product_detail('mock_id')
        assert product.name == expected_product_description['name']

    def test_register_product(self):
        uid, name, description, price, stock, image = expected_product_description.values()
        product_entity = self.product_factory.create(None, name, description, float(price), int(stock), image)
        product = self.product_service.register_product(product_entity)
        assert type(product) is ProductEntity
        assert product.id == uid

    def test_update_product(self):
        uid, name, description, price, stock, image = expected_product_description.values()
        product_entity = self.product_factory.create(uid, name, description, price, stock, image)
        product = self.product_service.update_product(product_entity)
        assert type(product) is ProductEntity
