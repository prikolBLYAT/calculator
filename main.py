def get_user_input():
    try:
        num1_input = input("Введите первое число (или 'q' для выхода): ")
        if num1_input.lower() == 'q':
            return None, None, None

        num1 = float(num1_input)
        operation = input("Введите операцию (+, -, *, /): ")

        num2_input = input("Введите второе число (или 'q' для выхода): ")
        if num2_input.lower() == 'q':
            return None, None, None

        num2 = float(num2_input)
        return num1, operation, num2

    except ValueError:
        print("Ошибка: нужно вводить числа!")
        return None, None, None


def calculate(num1, operation, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "Ошибка: аргументы должны быть числами"

    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "Ошибка: деление на ноль"
            return num1 / num2
        case _:
            return "Неизвестная операция"


def format_result(num1, operation, num2, result):
    if isinstance(result, str) and result.startswith("Ошибка"):
        return result
    return f"{num1} {operation} {num2} = {result}"


def main():
    print("Введите q для выхода\n")

    while True:
        num1, operation, num2 = get_user_input()
        if num1 is None:
            print("Выход из программы.")
            break

        result = calculate(num1, operation, num2)
        print(format_result(num1, operation, num2, result))
        print("---------------------------------")


if __name__ == "__main__":
    main()
