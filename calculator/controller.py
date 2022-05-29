import UI
import calculate
import view


def button_click():
    str_1 = UI.enter_user()
    list_1 = calculate.str_in_list(str_1)
    complex_1 = calculate.complex_result(list_1)
    view.view_data(complex_1)

    str_2 = UI.enter_user()
    list_2 = calculate.str_in_list(str_2)
    complex_2 = calculate.complex_result(list_2)
    view.view_data(complex_2)

    user_symbol = UI.math_symbol()
    result = calculate.result(user_symbol, complex_1, complex_2)
    view.view_data(f'Результат: {result}')
