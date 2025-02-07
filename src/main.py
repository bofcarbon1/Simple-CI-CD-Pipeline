# Main functions calls our simple functions
from src import simple_functions
from src.simple_functions import add


def print_result(p_result):
    # Use a breakpoint in the src line below to debug your script.
    print(f'Result is: : {p_result}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    result = add(2, 2)
    print_result(result)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
