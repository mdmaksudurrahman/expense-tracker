import json
import os

DATA_FILE = "data.json"


def load_expenses(filepath=DATA_FILE):
    """Load expenses from a JSON file.

    Returns an empty list if the file doesn't exist yet."""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r") as f:
        return json.load(f)


def save_expenses(expenses, filepath=DATA_FILE):
    """Write the full list of expenses back to the JSON file."""
    with open(filepath, "w") as f:
        json.dump(expenses, f, indent=2)


def add_expense(amount, category, date, filepath=DATA_FILE):
    """Add a new expense and persist it. Raises ValueError on invalid input."""
    if amount <= 0:
        raise ValueError("Amount must be positive.")

    expenses = load_expenses(filepath)
    expenses.append({"amount": amount, "category": category, "date": date})
    save_expenses(expenses, filepath)
    return expenses
