import pytest
from app.infrastructure.fast_api import create_app
from fastapi.testclient import TestClient
from app.test import create_mock_product_repository, expected_products_catalog, expected_product_description


class TestUserApi:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.app = create_app()
        self.client = TestClient(self.app)
        self.base_path = '/products'

    def test_get_product_catalog(self):
        with self.app.container.product_repository.override(create_mock_product_repository()):
            response = self.client.get(self.base_path + '/')
            assert expected_products_catalog == response.json()
            assert response.status_code == 200

    def test_get_product_detail(self):
        with self.app.container.product_repository.override(create_mock_product_repository()):
            response = self.client.get(self.base_path + '/mock_id')
            assert expected_product_description == response.json()
            assert response.status_code == 200

    def test_post_register_product(self):
        with self.app.container.product_repository.override(create_mock_product_repository()):
            response = self.client.post(
                self.base_path,
                json=expected_product_description
            )
            assert expected_product_description == response.json()
            assert response.status_code == 200

    def test_put_update_product(self):
        with self.app.container.product_repository.override(create_mock_product_repository()):
            response = self.client.put(
                self.base_path + '/mock_id',
                json=expected_product_description
            )
            assert expected_product_description == response.json()
            assert response.status_code == 200