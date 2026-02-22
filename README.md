# Calculator App UI Test

This repository contains an automated UI test for the Windows Calculator app using `pytest` and `pywinauto`.

## What This Test Covers

The test in `test_calculator.py` launches Calculator and validates:

- `5 + 3 = 8`
- `10 - 4 = 6`

It then closes the Calculator window.

## Prerequisites

- Windows (Calculator is launched via `calc.exe`)
- Python 3.10+ (recommended)

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```powershell
pip install pytest pywinauto
```

## Run Tests

From the project root:

```powershell
pytest -v
```

## Notes

- This is a UI automation test, so the desktop session must be active.
- If your system language changes Calculator button labels, locators may need updates in `test_calculator.py`.
