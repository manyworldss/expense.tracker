Python Expense Tracker
A simple Python application for tracking personal expenses using dataclasses and type hints.
Features

Track expenses (amount, category, description)
Automatic date tracking
CSV export functionality

Usage

Create a new expense
expense = Expense(
    amount=50.0,
    category="Food",
    description="Grocery shopping"
)

# With custom date
from datetime import datetime
expense = Expense(
    amount=100.0,
    category="Transportation",
    description="Train ticket",
    date=datetime(2024, 1, 15)
)

Requirements

Python 3.7+

No external dependencies

Structure

The Expense class stores:

Amount (float)
Category (str)
Description (str)
Date (Optional[datetime]) - defaults to the current date

Future Features:

Data visualization

Budget tracking

GUI interface

Database storage

License
MIT
