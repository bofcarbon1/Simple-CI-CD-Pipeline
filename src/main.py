# Import the source functions to test
from src.simple_functions import add
from src.simple_apis import check_balance


def print_result(p_result):
    print(f'Result is: : {p_result}')  # Press Ctrl+F8 to toggle the breakpoint.


# Starts the application
if __name__ == '__main__':
    # simple functions
    result = add(2, 2)
    print_result(result)
    # simple api calls
    api_result = check_balance(3032158102)
    print_result(api_result)
