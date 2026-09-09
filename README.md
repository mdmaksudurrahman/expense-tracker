# Expense Tracker (CLI)

![CI](https://github.com/mdmaksudurrahman/expense-tracker/actions/workflows/ci.yml/badge.svg)

A command-line expense tracker built in Python. Add, view, and summarize personal expenses, with data persisted to a local JSON file. Built as a foundational project to demonstrate clean Python fundamentals — file I/O, data structures, error handling, and disciplined testing/CI practices — as part of a project-based portfolio.

## Features

- Add an expense with amount, category, and date
- View all recorded expenses
- Filter expenses by category or date range
- Generate a summary report (total spend, spend by category)
- Data persisted locally in `data.json`
- Input validation with clear error handling (e.g., negative amounts, invalid dates)

## Tech Stack

- Python 3.12
- `pytest` for unit testing
- `flake8` for linting
- `black` for code formatting
- GitHub Actions for CI

## Project Structure
expense-tracker/
├── src/
│ └── tracker.py
├── tests/
│ └── test_tracker.py
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md


## Installation

```bash
git clone https://github.com/mdmaksudurrahman/expense-tracker.git
cd expense-tracker
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

```bash
python src/tracker.py add --amount 50 --category food --date 2026-09-01
python src/tracker.py list
python src/tracker.py report
```

*(Update this section with your actual CLI commands once built — argparse or click syntax.)*

## Running Tests

```bash
pytest -v
pytest --cov=src tests/     # with coverage report
```

## Linting & Formatting

```bash
flake8 src/ tests/
black src/ tests/
```

## CI/CD

Every push and pull request triggers GitHub Actions to run linting and the full test suite. Merges to `main` require passing CI checks. See `.github/workflows/ci.yml` for details.

## Roadmap

- [ ] Add category-based budgeting limits
- [ ] Export report to CSV
- [ ] Add currency support (AED/QAR)

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.