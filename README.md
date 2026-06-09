# Upgraded ATM Machine Project

## Improvements Made

1.  **Object-Oriented Programming (OOP)**: Refactored the code into an `ATM` class for better modularity and maintainability.
2.  **Data Persistence**: Integrated a JSON-based storage system (`atm_data.json`). Unlike the original version where the balance resets every time the program restarts, this version remembers your balance and transaction history.
3.  **Authentication System**: Added account number and PIN-based login. It includes a security feature that limits PIN attempts to 3.
4.  **Transaction History**: Every withdrawal and deposit is logged with a timestamp, allowing users to view their past transactions.
5.  **Robust Error Handling**: Added `try-except` blocks and input validation to prevent the program from crashing on invalid user input (e.g., entering text instead of numbers).
6.  **Advanced Features**: Added the ability to change the account PIN securely.
7.  **Clean User Interface**: Improved formatting and a clear menu system for a better user experience.

## How to Run

1.  Ensure you have Python installed.
2.  Navigate to the `atm_machine_project` directory.
3.  Run the main script:
    ```bash
    python main.py
    ```

## Default Credentials

The system comes pre-configured with two accounts:
- **Account 1**: `123456` (PIN: `1234`)
- **Account 2**: `654321` (PIN: `4321`)

*Note: Changes to PINs and balances will be saved to `atm_data.json`.*
