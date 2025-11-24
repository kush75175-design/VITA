# ATM Facilitator Software for Children (With Digit-to-Word Converter)

## Overview
This project is a simple Python program that acts as an ATM designed for children.  
It allows the user to withdraw money, deposit money, or check the balance.  
After each operation, the final amount is converted into words.

The program also includes a loop so the user can run multiple transactions until they choose to exit.

---

## Features
- Starting balance: 65986
- Options:
  - A → Withdraw
  - B → Deposit
  - K → Check Balance
  - X → Exit Program
- Converts numerical balance into words (supports 1–5 digit numbers)
- Restriction for children’s account:
  - If the amount has 6 or more digits, the program displays:
    "CHILDREN ACCOUNT DO NOT ALLOW AMOUNT ABOVE 100000"
- Handles incorrect input safely (invalid amount or invalid menu option)

---

## How the Program Works
1. The user selects an option (A, B, K, or X).
2. For Withdraw or Deposit, the user enters an amount.
3. The program updates the balance.
4. The balance is converted into words using digit-by-digit dictionaries.
5. The user is asked whether they want to use the ATM again.
6. The loop continues until the user selects N or presses X to exit.

---

## How to Run the Program
1. Install Python 3 on your system.
2. Save the code into a file, e.g., `atm_children.py`.
3. Run it using:
