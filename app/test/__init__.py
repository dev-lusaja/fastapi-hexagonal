from unittest.mock import Mock, patch
from app.domain.entities.product import ProductEntityFactory
from app.domain.repositories.product import ProductRepository
from app.test.data.product import expected_products_catalog, expected_product_description


product_data = {'id': 'MockID', 'name': 'MockProduct', 'description': 'MockDescription', 'price': 10, 'stock': 1, 'image': 'MockImage.jpg'}
product_repository_get_all = [product_data for x in range(2)]
product_repository_get_by_id = product_data

@patch('app.infrastructure.repositories.product.ProductInMemoryRepository', spec=True)
def create_mock_product_repository(mock_repository: Mock):
    mock_product_repo: ProductRepository = mock_repository.return_value
    mock_product_repo.get_all = Mock(return_value=[ProductEntityFactory.create(**product) for product in product_repository_get_all])
    mock_product_repo.get_by_id = Mock(return_value=ProductEntityFactory.create(**product_repository_get_by_id))
    mock_product_repo.add = Mock(return_value=ProductEntityFactory.create(**product_repository_get_by_id))
    mock_product_repo.update = Mock(return_value=ProductEntityFactory.create(**product_repository_get_by_id))
    return mock_product_repo
