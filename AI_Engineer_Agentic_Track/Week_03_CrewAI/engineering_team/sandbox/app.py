import gradio as gr
from main import TradingSystem

# Create an instance of the TradingSystem
trading_system = TradingSystem()

# Gradio Interface Functions

def create_account(account_id):
    try:
        trading_system.create_account(account_id)
        return f"Account '{account_id}' created successfully."
    except ValueError as e:
        return str(e)


def deposit_funds(account_id, amount):
    try:
        trading_system.accounts[account_id].deposit(amount)
        return f"Deposited ${amount} to account '{account_id}'. New balance: ${trading_system.accounts[account_id].balance:.2f}."
    except Exception as e:
        return str(e)


def withdraw_funds(account_id, amount):
    try:
        trading_system.accounts[account_id].withdraw(amount)
        return f"Withdrew ${amount} from account '{account_id}'. New balance: ${trading_system.accounts[account_id].balance:.2f}."
    except Exception as e:
        return str(e)


def buy_shares(account_id, symbol, quantity):
    try:
        trading_system.accounts[account_id].buy_shares(symbol, quantity)
        return f"Bought {quantity} shares of '{symbol}' for account '{account_id}'."
    except Exception as e:
        return str(e)


def sell_shares(account_id, symbol, quantity):
    try:
        trading_system.accounts[account_id].sell_shares(symbol, quantity)
        return f"Sold {quantity} shares of '{symbol}' from account '{account_id}'."
    except Exception as e:
        return str(e)


def get_portfolio(account_id):
    try:
        holdings = trading_system.get_user_portfolio(account_id)
        return holdings
    except Exception as e:
        return str(e)


def calculate_profit(account_id):
    try:
        profit_or_loss = trading_system.calculate_profit_or_loss(account_id)
        return f"Profit/Loss for account '{account_id}': ${profit_or_loss:.2f}"
    except Exception as e:
        return str(e)


def get_transactions(account_id):
    try:
        transactions = trading_system.accounts[account_id].get_transactions()
        return [
            {"Transaction ID": tx.transaction_id,
             "Action": tx.action,
             "Amount": tx.amount,
             "Quantity": tx.quantity,
             "Symbol": tx.symbol,
             "Timestamp": tx.timestamp}
            for tx in transactions
        ]
    except Exception as e:
        return str(e)

# Gradio UI Components
with gr.Blocks() as demo:
    gr.Markdown("# Trading Simulation Platform")

    account_id_input = gr.Textbox(label="Account ID")
    create_button = gr.Button(value="Create Account")
    create_output = gr.Textbox(label="Account Creation Output")

    deposit_input = gr.Number(label="Deposit Amount")
    deposit_button = gr.Button(value="Deposit")
    deposit_output = gr.Textbox(label="Deposit Output")

    withdraw_input = gr.Number(label="Withdraw Amount")
    withdraw_button = gr.Button(value="Withdraw")
    withdraw_output = gr.Textbox(label="Withdraw Output")

    buy_symbol_input = gr.Textbox(label="Buy Symbol")
    buy_quantity_input = gr.Number(label="Buy Quantity")
    buy_button = gr.Button(value="Buy Shares")
    buy_output = gr.Textbox(label="Buy Output")

    sell_symbol_input = gr.Textbox(label="Sell Symbol")
    sell_quantity_input = gr.Number(label="Sell Quantity")
    sell_button = gr.Button(value="Sell Shares")
    sell_output = gr.Textbox(label="Sell Output")

    portfolio_button = gr.Button(value="Get Portfolio")
    portfolio_output = gr.JSON(label="Portfolio")

    profit_button = gr.Button(value="Calculate Profit/Loss")
    profit_output = gr.Textbox(label="Profit/Loss Output")

    transactions_button = gr.Button(value="Get Transactions")
    transactions_output = gr.JSON(label="Transactions")

    # UI Logic
    create_button.click(create_account, inputs=account_id_input, outputs=create_output)
    deposit_button.click(deposit_funds, inputs=[account_id_input, deposit_input], outputs=deposit_output)
    withdraw_button.click(withdraw_funds, inputs=[account_id_input, withdraw_input], outputs=withdraw_output)
    buy_button.click(buy_shares, inputs=[account_id_input, buy_symbol_input, buy_quantity_input], outputs=buy_output)
    sell_button.click(sell_shares, inputs=[account_id_input, sell_symbol_input, sell_quantity_input], outputs=sell_output)
    portfolio_button.click(get_portfolio, inputs=account_id_input, outputs=portfolio_output)
    profit_button.click(calculate_profit, inputs=account_id_input, outputs=profit_output)
    transactions_button.click(get_transactions, inputs=account_id_input, outputs=transactions_output)

# If this module is run, launch the Gradio UI
if __name__ == '__main__':
    demo.launch(debug=True)