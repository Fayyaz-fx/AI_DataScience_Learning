from typing import Dict

class Portfolio:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        self.holdings: Dict[str, int] = {}

    def add_shares(self, symbol: str, quantity: int) -> None:
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity

    def remove_shares(self, symbol: str, quantity: int) -> None:
        if self.holdings.get(symbol, 0) < quantity:
            raise ValueError('Not enough shares to remove')
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]

    def calculate_total_value(self) -> float:
        total_value = 0.0
        for symbol, quantity in self.holdings.items():
            total_value += get_share_price(symbol) * quantity
        return total_value

    def get_holdings(self) -> Dict[str, int]:
        return self.holdings


def get_share_price(symbol: str) -> float:
    # Mock share prices for the demo
    prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)
