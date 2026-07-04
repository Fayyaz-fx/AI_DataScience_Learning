```markdown
# Detailed Design for Account Management System

## Modules Overview

The system will be broken down into three main modules:
1. **Account Management Module**: Handles user accounts and transactions.
2. **Portfolio Module**: Manages user holdings and portfolio calculations.
3. **API Module**: Integration with the Gradio frontend for displaying information and receiving user input.

### Module 1: Account Management Module

#### Classes
- **Account**
  - Attributes:
    - `user_id: str`
    - `balance: float`
    - `transactions: List[Transaction]`
  - Methods:
    - `create_account(user_id: str) -> None`
    - `deposit(amount: float) -> None`
    - `withdraw(amount: float) -> None`
    - `buy_shares(symbol: str, quantity: int) -> None`
    - `sell_shares(symbol: str, quantity: int) -> None`
    - `get_transactions() -> List[Transaction]`

- **Transaction**
  - Attributes:
    - `transaction_id: str`
    - `timestamp: datetime`
    - `action: str` (buy/sell/deposit/withdraw)
    - `amount: float`
    - `quantity: int`
    - `symbol: str`
  - Methods:
    - `__init__(action: str, amount: float, quantity: int, symbol: str) -> None`

#### Function Signatures
- `def get_share_price(symbol: str) -> float`
- `def get_user_portfolio(user_id: str) -> Dict[str, float]`
- `def calculate_profit_or_loss(user_id: str) -> float`

### Module 2: Portfolio Module

#### Classes
- **Portfolio**
  - Attributes:
    - `user_id: str`
    - `holdings: Dict[str, int]`
  - Methods:
    - `add_shares(symbol: str, quantity: int) -> None`
    - `remove_shares(symbol: str, quantity: int) -> None`
    - `calculate_total_value() -> float`
    - `get_holdings() -> Dict[str, int]`

### Module 3: API Module (Gradio Frontend Integration)

#### Functions
- `def launch_interface() -> None`
  - Description: Initializes and launches the Gradio interface.

#### Components
- **Input Components**:
  - `account_id_input: gradio.inputs.Textbox`
  - `deposit_input: gradio.inputs.Number`
  - `withdraw_input: gradio.inputs.Number`
  - `buy_shares_input: gradio.inputs.Textbox`
  - `sell_shares_input: gradio.inputs.Textbox`
  - `quantity_input: gradio.inputs.Number`

- **Output Components**:
  - `portfolio_output: gradio.outputs.JSON`
  - `profit_loss_output: gradio.outputs.Textbox`
  - `transactions_output: gradio.outputs.JSON`

#### Functions to Handle Inputs:
- `def handle_deposit(account_id: str, amount: float) -> None`
- `def handle_withdraw(account_id: str, amount: float) -> None`
- `def handle_buy_shares(account_id: str, symbol: str, quantity: int) -> None`
- `def handle_sell_shares(account_id: str, symbol: str, quantity: int) -> None`
- `def display_portfolio(account_id: str) -> Dict[str, float]`
- `def display_transactions(account_id: str) -> List[Transaction]`
- `def display_profit_or_loss(account_id: str) -> float`

## Assignments

### Backend Engineer
- **Responsibilities**:
  - Implement the Account Management Module and Portfolio Module.
  - Write the logic for all class methods and function signatures defined in these modules.
  
### Frontend Engineer
- **Responsibilities**:
  - Develop the Gradio application using the API Module functions.
  - Ensure the correct Gradio components are utilized for user interaction according to Gradio 6 specifications.
  - Follow the latest Gradio 6 API changes:
    - Utilize `gr.inputs` and `gr.outputs` correctly.
    - Ensure that `launch_interface()` is called to start the Gradio app.

### Test Engineer
- **Responsibilities**:
  - Write unit tests for the backend module, ensuring coverage for all methods in both the Account and Portfolio classes.
  - Validate transaction logic, account balance restrictions, and portfolio calculations.
  - Implement tests for edge cases such as overdraft attempts and selling non-existent shares.
  
## Success Criteria
- The system is successfully built, all modules interact seamlessly, and all functionalities meet the outlined requirements.
- The frontend displays information accurately and allows user interactions without errors.
- Unit tests demonstrate that the backend works correctly, and all edge cases are handled.
```