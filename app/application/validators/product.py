from app.domain.exceptions import InvalidPrice, InvalidDescription


class ProductValidator:

    @staticmethod
    def validate_price_is_float(price: float) -> float:
        try:
            float(price)
        except ValueError:
            raise InvalidPrice
        return float(price)

    @staticmethod
    def validate_description_len(description: str) -> None:
        if len(description) > 50:
            raise InvalidDescription
