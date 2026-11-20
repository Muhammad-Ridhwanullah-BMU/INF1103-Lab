
from Product import Product
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct
from Supplier import Supplier


class ProductFactory:

    @staticmethod
    def create(
        product_type: str,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier,
        *,
        weight: float | None = None,
        download_size: float | None = None
    ) -> Product:

        if not isinstance(product_type, str):
            raise ValueError("Product type must be text.")

        product_type = product_type.strip().lower()

        if product_type == "physical":

            if weight is None:
                raise ValueError("Physical product requires weight.")

            if download_size is not None:
                raise ValueError(
                    "Physical product cannot have download size."
                )

            return PhysicalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                supplier,
                weight
            )

        elif product_type == "digital":

            if download_size is None:
                raise ValueError(
                    "Digital product requires download size."
                )

            if weight is not None:
                raise ValueError(
                    "Digital product cannot have weight."
                )

            return DigitalProduct(
                product_id,
                name,
                price,
                stock_quantity,
                supplier,
                download_size
            )

        else:
            raise ValueError(
                f"Unknown product type: {product_type}"
            )
