# Personal Expense Tracker v1.3

An improved version of a(not published or debugged) Python command-line application for managing personal income and expenses, featuring JSON data persistence, transaction deletion, and automatic date and time tracking.

## Features

- Add income transactions.
- Add expense transactions.
- Organize expenses into categories:
  - Food
  - Transport
  - Education
  - Entertainment
  - Other
- View complete transaction history.
- Calculate total income and expenses.
- Display current account balance.
- View expenses by category.
- Save transaction details, including date and time, in a JSON file.
- Automatically load previously saved transactions when the application starts.
## New Features

- Delete existing transactions.
- Automatically record the date and time of each transaction.

## Technologies Used

- Python
- JSON
- Datetime
- Built-in Python functions and data structures

## Data Storage

The application uses a JSON file (`transaction.json`) for persistent transaction storage.

Each transaction includes relevant information such as:

- Transaction type
- Amount
- Description
- Category (for expenses)
- Automatically generated date and time

The stored date and time are also displayed in the transaction history.

## How to Run

1. Make sure Python is installed.
2. Download or clone this repository.
3. Run the Python file:

```bash
python "Expense Tracker v1.3.py"
```

## Project Version

**Version:** 1.3

**Type:** Command-Line Application (CLI)

**Status:** Under Development

## About

This project is part of my Python programming learning journey. Version 1.3 builds upon the original expense tracker by introducing transaction deletion, automatic date and time tracking, and improved JSON data management.

The project focuses on practical Python programming, data handling, and incremental software development.

Thank you for reading. HJ