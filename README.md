<p align="center">
  <a href="https://stellarburgers.education-services.ru/" target="_blank">
    <img width="120" height="auto" src="https://stellarburgers.education-services.ru/favicon.ico" title="Перейти на Stellar Burgers" alt="Stellar Burgers">
  </a>
</p>

# Проект автоматизации тестирования сервиса [Stellar Burgers](https://stellarburgers.education-services.ru/)
#### Основа для написания автотестов — фреймворк _Selenium_. Также использовались библиотеки: PyTest, Faker.

## Проверки:
### - Регистрация в файле _test_registration_page.py_:
**test_registration_success** - проверка успешной регистрации пользователя\
**test_registration_password_with_five_symbols_show_error_text** - проверка отображения ошибки при некорректном поле Пароля\
**test_registration_failed** - проверка отображения ошибки при попытке зарегистрировать существующего пользователя

### - Авторизация в файле _test_login_page.py_:
**test_login_success** - проверка аутентификации пользователя\
**test_click_log_in_account_button_on_main_page_redirects_to_login_success** - проверка перехода на страницу Login по кнопке 'Войти в аккаунт' на главной\
**test_click_personal_cabinet_button_redirects_to_login_success** - проверка перехода на страницу Login по кнопке 'Личный Кабинет'\
**test_click_log_in_via_button_registration_form_redirects_to_login_success** - проверка перехода на страницу Login через кнопку в форме регистрации\
**test_click_log_in_button_in_password_recovery_redirects_to_login_success** - проверка перехода на страницу Login через кнопку в форме восстановления пароля

### - Личный кабинет в файле _test_profile_page.py_:
**test_click_personal_account_button_redirects_personal_account_page_success** - проверка перехода на страницу Личный Кабинет по клику на 'Личный кабинет'\
**test_navigate_from_personal_account_to_constructor_success** - проверка перехода из личного кабинета в конструктор\
**test_account_logout_success** - проверка выхода по кнопке 'Выйти' в личном кабинете

### - Раздел «Конструктор» в файле _test_constructor_page.py_:
**test_section_navigation_success** - проверка переходов между разделами\
**test_navigate_to_breads_section_success** - проверка перехода к разделу 'Булки'

## Установка зависимостей:
```
pip3 install -r requirements.txt
```
##### Для Python второй версии:
```
pip install -r requirements.txt
```

## Запуск тестов:
```
pytest tests
```
