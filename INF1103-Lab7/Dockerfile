FROM python:3.12-slim

WORKDIR /app

COPY App.py FileHandler.py Inventory.py Product.py inventory.json DigitalProduct.py PhysicalProduct.py CanBeShipped.py ./

CMD ["python", "App.py"]
