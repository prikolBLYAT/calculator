from input_part import get_user_input
from calc_part import calculate
from format_part import format_result

def main():
    num1, operation, num2 = get_user_input()
    if num1 is None:
        return
    result = calculate(num1, operation, num2)
    print(format_result(num1, operation, num2, result))

if __name__ == "__main__":
    main()
