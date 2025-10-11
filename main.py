from input_part import get_user_input
from calc_part import calculate
from format_part import format_result

def get_user_input():
    try:
        num1 = float(input("Введите первое число: "))
        operation = input("Введите операцию (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        return num1, operation, num2
    except ValueError:
        print("Ошибка: нужно вводить числа!")
        return None, None, None

def main():
    num1, operation, num2 = get_user_input()
    if num1 is None:
        return
    result = calculate(num1, operation, num2)
    print(format_result(num1, operation, num2, result))

if __name__ == "__main__":
    main()
def calculate(num1, operation, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неизвестная операция"
