from datetime import datetime      # For handling dates
from dataclasses import dataclass  # Makes creating classes easier 
from typing import Optional        # For type hinting 

@dataclass
class Expense:
       # These are the class attributes with type hints
    amount: float 
    category: str
    description: str
    date: Optional[datetime] = None # 

    def __post_init__(self): 
        # This method runs after __init__
        # If no date provided, use current date/time
        if self.date is None:
            self.date = datetime.now()
    
    def format_date(self) -> str:
        # Returns date in readable format: YYYY-MM-DD
        return self.date.strftime("%Y-%m-%d")
    def to_csv_line(self) -> list:
        # Convert expense to list format for csv storage
        return [
            str(self.amount),
            self.category,
            self.description,
            self.format_date()
        ]
    
if __name__ == "__main__":

    # Test creating an expense
    expense = Expense(
        amount=50.0,
        category="Food",
        description="Grocery shopping"
    )
    
    # Print the expense to verify it works
    print(f"Amount: ${expense.amount}")
    print(f"Category: {expense.category}")
    print(f"Description: {expense.description}")
    print(f"Date: {expense.format_date()}")