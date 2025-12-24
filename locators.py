from selenium.webdriver.common.by import By


class Locators:
    # Локаторы для регистрации/авторизации
    NAME = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Имя']/following-sibling::input")  # Поле имя
    EMAIL = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Email']/following-sibling::input")  # Поле email
    PASSWORD = (By.XPATH, "//label[@class='input__placeholder text noselect text_type_main-default' and text()='Пароль']/following-sibling::input")  # Поле пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка "Войти" на странице авторизации
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and text()='Личный Кабинет']")  # Кнопка "Личный Кабинет" на главной странице
    # Вход на страницах регистрации и восстановления пароля
    LINK_LOGIN = (By.XPATH, "//a[@class='Auth_link__1fOlj' and text()='Войти']")  # Кнопка "Войти"
    # Ошибка при регистрации уже существующего пользователя
    ERROR_REG_MESSAGE_EXIST_USER = (By.XPATH, "//main/div/p[@class='input__error text_type_main-default']")  # Текст ошибки "Такой пользователь уже существует"
    # Ошибка при регистрации с невалидным паролем
    ERROR_REG_MESSAGE_PASSWORD = (By.XPATH, "//form/fieldset//p[@class='input__error text_type_main-default' and text()='Некорректный пароль']")  # Текст ошибки "Некорректный пароль"

    # Локатор после авторизации
    PLACE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"

    # Локаторы из header
    CONSTRUCTOR_BUTTON = (By.XPATH, "//header/nav/ul/li//p[text()='Конструктор']")  # Кнопка "Конструктор"
    LOGO_BUTTON = (By.XPATH, "//header/nav/div[@class='AppHeader_header__logo__2D0X2']/a")  # Логотип-кнопка "Stellar Burgers"

    # Локаторы на странице Личный Кабинет
    SIGNOUT_BUTTON = (By.XPATH, "//main/div/nav//button[text()='Выход']")  # Кнопка "Выход"

    # Локаторы для раздела "Конструктор"
    TAB_BREADS = (By.XPATH, "//main/section//span[text()='Булки']")  # Раздел "Булки"
    TAB_SAUCES = (By.XPATH, "//main/section//span[text()='Соусы']")  # Раздел "Соусы"
    TAB_TOPPINGS = (By.XPATH, "//main/section//span[text()='Начинки']")  # Раздел "Начинки"
    SECTION_SELECTED_CONSTRUCTOR = (By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']/span")  # Выбранный раздел
