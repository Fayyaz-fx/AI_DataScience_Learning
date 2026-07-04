from datetime import datetime
from typing import List, Dict

class Transaction:
    def __init__(self, action: str, amount: float, quantity: int, symbol: str) -> None:
        self.transaction_id = f'{action[0].upper()}{int(datetime.now().timestamp())}'
        self.timestamp = datetime.now()
        self.action = action
        self.amount = amount
        self.quantity = quantity
        self.symbol = symbol

class Account:
    def __init__(self, user_id: str) -> None:
        self.user_id = user_id
        self.balance = 0.0
        self.transactions: List[Transaction] = []
        self.holdings: Dict[str, int] = {}

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(Transaction('deposit', amount, 0, ''))

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        self.transactions.append(Transaction('withdraw', amount, 0, ''))

    def buy_shares(self, symbol: str, quantity: int) -> None:
        total_cost = get_share_price(symbol) * quantity
        if total_cost > self.balance:
            raise ValueError('Not enough balance to buy shares')
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append(Transaction('buy', total_cost, quantity, symbol))

    def sell_shares(self, symbol: str, quantity: int) -> None:
        if self.holdings.get(symbol, 0) < quantity:
            raise ValueError('Not enough shares to sell')
        total_value = get_share_price(symbol) * quantity
        self.balance += total_value
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append(Transaction('sell', total_value, quantity, symbol))

    def get_transactions(self) -> List[Transaction]:
        return self.transactions


def get_share_price(symbol: str) -> float:
    # Mock share prices for the demo
    prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)
