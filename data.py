class Credentials:
    name = "Мелисса"
    email = "melissapowell36854@yahoo.com"
    password = "987654321"

class ExpectedValueConstructorPage:

    text_order_button = "Оформить заказ"  # Кнопка "Оформить заказ" после аутентификации

    # Разделы в конструкторе
    text_tab_breads = "Булки"
    text_tab_sauces = "Соусы"
    text_tab_toppings = "Начинки"

class ExpectedValueLoginPage:

    text_link_login = "Войти"  # Текст кнопки "Войти"

class ExpectedValueRegistrationPage:

    text_error_invalid_password = "Некорректный пароль"  # Текст ошибки при некорректном пароле
    text_error_repeated_registering_user = "Такой пользователь уже существует"  # Текст ошибки при регистрации существующего пользователя
