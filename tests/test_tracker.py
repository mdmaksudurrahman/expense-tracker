import pytest
from src.tracker import add_expense, load_expenses


def test_add_expense_saves_to_file(tmp_path):
    filepath = tmp_path / "data.json"

    add_expense(50, "Food", "2026-090=-01", filepath=str(filepath))

    expenses = load_expenses(str(filepath))
    assert len(expenses) == 1
    assert expenses[0]["amount"] == 50.0
    assert expenses[0]["category"] == "Food"


def test_add_expense_rejects_negative_amount(tmp_path):
    filepath = tmp_path / "data.json"

    with pytest.raises(ValueError):
        add_expense(-10, "Food", "2026-09-01", filepath=str(filepath))
