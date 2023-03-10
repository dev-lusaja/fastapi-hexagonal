from dependency_injector import containers, providers
from app.domain.entities.product import ProductEntityFactory
from app.infrastructure.events.product import ProductCreatedQueueEvent, ProductUpdatedQueueEvent
from app.infrastructure.handlers import Handlers
from app.infrastructure.repositories.product import ProductInMemoryRepository
from app.application.services.product import ProductService


class Container(containers.DeclarativeContainer):

    #loads all handlers where @injects are set
    wiring_config = containers.WiringConfiguration(modules=Handlers.modules())

    #Factories
    product_factory = providers.Factory(ProductEntityFactory)

    #Repositories
    product_repository = providers.Singleton(ProductInMemoryRepository)

    #Events
    product_created_event = providers.Factory(ProductCreatedQueueEvent)
    product_updated_event = providers.Factory(ProductUpdatedQueueEvent)

    #Services
    product_services = providers.Factory(ProductService, product_repository, product_created_event, product_updated_event)
