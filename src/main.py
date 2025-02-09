# Import the source functions to test
from src.simple_functions import add


def print_result(p_result):
    print(f'Result is: : {p_result}')  # Press Ctrl+F8 to toggle the breakpoint.


# Starts the application
if __name__ == '__main__':
    result = add(2, 2)
    print_result(result)
