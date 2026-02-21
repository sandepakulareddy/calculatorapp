from pywinauto.application import Application
from pywinauto import Desktop
import time


def test_calculator_operations():

    # Launching Calculator
    app = Application(backend="uia").start("calc.exe")
    time.sleep(2)

    calc = Desktop(backend="uia").window(title="Calculator")

    # Addition
    calc.child_window(title="Five", control_type="Button").click()
    calc.child_window(title="Plus", control_type="Button").click()
    calc.child_window(title="Three", control_type="Button").click()
    calc.child_window(title="Equals", control_type="Button").click()

    result = calc.child_window(auto_id="CalculatorResults").window_text()
    assert "8" in result

    # clear
    calc.child_window(title="Clear", control_type="Button").click()

    # Subtraction
    calc.child_window(title="One", control_type="Button").click()
    calc.child_window(title="Zero", control_type="Button").click()
    calc.child_window(title="Minus", control_type="Button").click()
    calc.child_window(title="Four", control_type="Button").click()
    calc.child_window(title="Equals", control_type="Button").click()

    result2 = calc.child_window(auto_id="CalculatorResults").window_text()
    assert "6" in result2

    # Close Calculator
    calc.close()