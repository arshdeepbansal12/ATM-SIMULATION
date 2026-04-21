ATM Simulation System (Python)
A modular, console-based ATM (Automated Teller Machine) simulation built with Python. This project demonstrates the use of modular programming, state management using parallel lists, and control flow logic to simulate real-world banking operations.

🚀 Features
Account Creation: Users can register by providing a name, unique User ID, and a secure PIN.

Secure Authentication: Access to banking features (Balance, Deposit, Withdraw) is protected by ID and PIN verification.

Transaction History: A detailed "Bank Statement" feature that logs every deposit and withdrawal made during the session.

Dynamic Balance Updates: Real-time calculation of balances with built-in validation for insufficient funds.

Modular Architecture: The logic is split across multiple files (deposit.py, withdraw.py, balance.py, etc.) for better maintainability and cleaner code.

📁 Project Structure
main.py: The entry point of the application containing the primary menu loop.

accounts.py: Handles the registration of new users and initializes account data.

utils.py: The central data hub storing user profiles, credentials, and transaction logs.

deposit.py / withdraw.py: Core logic for managing financial transactions.

balance.py: Allows users to view their current available funds.

statement.py: Tracks and displays the history of all session activities.

🛠️ Technical Skills Demonstrated
Python Fundamentals: Using lists, loops, and conditional statements.

Data Structures: Implementing parallel lists to map user data across different attributes.

Input Validation: Ensuring users enter valid IDs and have enough balance before processing transactions.

Modularization: Organizing a codebase into logical components and using Python imports effectively.
