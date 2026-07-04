from account import Account
from portfolio import Portfolio

class TradingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, user_id: str) -> Account:
        if user_id in self.accounts:
            raise ValueError('Account already exists')
        account = Account(user_id)
        self.accounts[user_id] = account
        return account

    def get_user_portfolio(self, user_id: str) -> Dict[str, float]:
        account = self.accounts.get(user_id)
        if not account:
            raise ValueError('Account does not exist')
        portfolio = Portfolio(user_id)
        for transaction in account.get_transactions():
            if transaction.action == 'buy':
                portfolio.add_shares(transaction.symbol, transaction.quantity)
            elif transaction.action == 'sell':
                portfolio.remove_shares(transaction.symbol, transaction.quantity)
        return portfolio.get_holdings()

    def calculate_profit_or_loss(self, user_id: str) -> float:
        account = self.accounts.get(user_id)
        if not account:
            raise ValueError('Account does not exist')
        initial_investment = account.get_transactions()[0].amount if account.get_transactions() else 0
        current_value = account.balance + sum(get_share_price(symbol) * quantity for symbol, quantity in self.get_user_portfolio(user_id).items())
        return current_value - initial_investment


def get_share_price(symbol: str) -> float:
    # Mock share prices for the demo
    prices = {'AAPL': 150.0, 'TSLA': 700.0, 'GOOGL': 2800.0}
    return prices.get(symbol, 0.0)
