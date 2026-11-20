from DiscountStrategy import DiscountStrategy

class CHASDiscount(DiscountStrategy):

    DISCOUNT_RATES = {
        "green": 10,
        "orange": 15,
        "blue": 20
    }

    def __init__(self, card_colour: str) -> None:
        if not isinstance(card_colour, str):
            raise ValueError("Card colour must be a string.")

        card_colour = card_colour.strip().lower()

        if card_colour not in self.DISCOUNT_RATES:
            raise ValueError("Invalid CHAS card colour.")

        self.card_colour = card_colour
        self.percentage = self.DISCOUNT_RATES[card_colour]

    def apply(self, total: float) -> float:
        return total * (1 - self.percentage / 100)
