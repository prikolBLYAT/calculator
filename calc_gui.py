import pygame
import pygame_gui

# --- Функции калькулятора ---
def calculate(num1, operation, num2):
    op = operation.strip()  # убираем пробелы
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Ошибка: деление на ноль"
        return num1 / num2
    else:
        return "Неизвестная операция"

def format_result(num1, operation, num2, result):
    return f"{num1} {operation} {num2} = {result}"

# --- Инициализация Pygame и GUI ---
def main():
    pygame.init()
    window_size = (400, 300)
    window_surface = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Калькулятор GUI')
    manager = pygame_gui.UIManager(window_size)
    
    # Поля ввода
    input1 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((50, 50), (100, 30)),
        manager=manager
    )
    input2 = pygame_gui.elements.UITextEntryLine(
        relative_rect=pygame.Rect((250, 50), (100, 30)),
        manager=manager
    )
    
    # Комбо для операции
    operation = pygame_gui.elements.UIDropDownMenu(
        options_list=['+', '-', '*', '/'],
        starting_option='+',
        relative_rect=pygame.Rect((160, 50), (60, 30)),
        manager=manager
    )
    
    # Кнопка "Посчитать"
    button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((150, 120), (100, 40)),
        text='Посчитать',
        manager=manager
    )
    
    # Метка для результата
    result_label = pygame_gui.elements.UILabel(
        relative_rect=pygame.Rect((50, 200), (300, 30)),
        text='',
        manager=manager
    )
    
    clock = pygame.time.Clock()
    is_running = True
    
    # --- Основной цикл ---
    while is_running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
    
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == button:
                    try:
                        num1 = float(input1.get_text())
                        num2 = float(input2.get_text())
                        # Исправление: берём строку из tuple, если нужно
                        op = operation.selected_option
                        if isinstance(op, tuple):
                            op = op[0]
                        op = str(op).strip()
                        res = calculate(num1, op, num2)
                        text = format_result(num1, op, num2, res)
                    except ValueError:
                        text = "Ошибка: вводите числа!"
                    result_label.set_text(text)
    
            manager.process_events(event)
    
        manager.update(time_delta)
        window_surface.fill((0, 0, 0))
        manager.draw_ui(window_surface)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
