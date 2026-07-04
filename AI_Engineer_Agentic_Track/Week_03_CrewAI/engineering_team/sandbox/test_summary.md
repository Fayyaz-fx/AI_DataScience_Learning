```python
import unittest
from account import Account, Transaction, get_share_price
from portfolio import Portfolio
from main import TradingSystem

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account("user123")

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 0.0)

    def test_deposit(self):
        self.account.deposit(100.0)
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(len(self.account.get_transactions()), 1)
        self.assertEqual(self.account.get_transactions()[0].action, 'deposit')

    def test_withdraw(self):
        self.account.deposit(100.0)
        self.account.withdraw(50.0)
        self.assertEqual(self.account.balance, 50.0)

    def test_withdraw_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(50.0)

    def test_buy_shares(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 700.0)
        self.assertEqual(self.account.holdings['AAPL'], 2)

    def test_buy_shares_insufficient_balance(self):
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 10)

    def test_sell_shares(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.holdings['AAPL'], 1)
        self.assertEqual(self.account.balance, 850.0)

    def test_sell_shares_insufficient_quantity(self):
        self.account.deposit(1000.0)
        self.account.buy_shares('AAPL', 1)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 2)


class TestPortfolio(unittest.TestCase):
    def setUp(self):
        self.portfolio = Portfolio("user123")

    def test_add_shares(self):
        self.portfolio.add_shares('AAPL', 5)
        self.assertEqual(self.portfolio.holdings['AAPL'], 5)

    def test_remove_shares(self):
        self.portfolio.add_shares('AAPL', 5)
        self.portfolio.remove_shares('AAPL', 3)
        self.assertEqual(self.portfolio.holdings['AAPL'], 2)

    def test_remove_shares_insufficient_quantity(self):
        with self.assertRaises(ValueError):
            self.portfolio.remove_shares('AAPL', 1)

    def test_calculate_total_value(self):
        self.portfolio.add_shares('AAPL', 2)
        self.portfolio.add_shares('TSLA', 1)
        total_value = self.portfolio.calculate_total_value()
        self.assertEqual(total_value, 150.0 * 2 + 700.0 * 1)


class TestTradingSystem(unittest.TestCase):
    def setUp(self):
        self.trading_system = TradingSystem()

    def test_create_account(self):
        account = self.trading_system.create_account("user123")
        self.assertEqual(account.user_id, "user123")

    def test_create_duplicate_account(self):
        self.trading_system.create_account("user123")
        with self.assertRaises(ValueError):
            self.trading_system.create_account("user123")

    def test_get_user_portfolio(self):
        account = self.trading_system.create_account("user123")
        account.deposit(1000.0)
        account.buy_shares('AAPL', 2)
        portfolio = self.trading_system.get_user_portfolio("user123")
        self.assertEqual(portfolio['AAPL'], 2)

    def test_calculate_profit_or_loss(self):
        account = self.trading_system.create_account("user123")
        account.deposit(1500.0)
        account.buy_shares('AAPL', 2)
        profit_or_loss = self.trading_system.calculate_profit_or_loss("user123")
        self.assertEqual(profit_or_loss, (300.0) - 1500.0)

    def test_calculate_profit_or_loss_account_not_exist(self):
        with self.assertRaises(ValueError):
            self.trading_system.calculate_profit_or_loss("nonexistent_user")

if __name__ == '__main__':
    unittest.main()
```