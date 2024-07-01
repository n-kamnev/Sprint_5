# ___Автотесты для сервиса Stellar Burgers___

### ___Проект содержит:___

*** 

#### ___В файле test_enter_button.py класс TestButtonNavigation с тестовыми методами:___

* `test_enter_in_account_button - Проверяет вход по кнопке "Войти в аккаунт `
* `test_login_button_in_registration_form - Проверяет вход через кнопку в форме регистрации`
* `test_login_button_in_restore_password - Проверяет вход через кнопку в форме восстановления пароля`
* `test_personal_cabinet_button - Проверяет вход по кнопке "Личный кабинет`

#### ___В файле test_enter_to_cabinet_and_exit_to_cabinet.py класс TestPersonalCabinet с тестовыми методами:___

* `test_enter_in_personal_cabinet_by_button - Проверяет переход по клику на «Личный кабинет» `
* `test_quit_from_personal_cabinet_by_button - Проверяет выход по кнопке «Выйти» в личном кабинете`

#### ___В файле test_registration.py класс TestStellaBurgerRegistration с тестовыми методами:___

* `test_registration_password_error - Проверяет регистрацию с невалидным паролем `
* `test_successful_registration - Проверяет успешную регистрацию`

#### ___В файле test_section_constructor.py класс TestSwitchingInConstructor с тестовыми методами:___

* `test_switch_to_buns - Проверяет переход в раздел "Булки"`
* `test_switch_to_filings_section - Проверяет переход в раздел "Начинки"`
* `test_switch_to_sauces_section - Проверяет переход в раздел "Соусы"`

#### ___В файле test_transitions.py класс TestTransitionFromToConstructor с тестовыми методами:___

* `test_transition_click_button_constructor - Проверка перехода по клику на «Конструктор»`
* `test_transition_click_logo - Проверка перехода по клику на логотип Stellar Burgers`

#### ___В файле data.py класс StellaBurgerTestData с тестовыми данными зарегистрированного пользователя.___

#### ___В файле conftest.py:___

* `импортируется библиотека pytest для тестирования с использованием Selenium WebDriver и браузера Chrome`
* `фикстура driver, которая создаёт экземпляр браузера Chrome, переходит на указанный URL и возвращает этот экземпляр. Затем в тестовой функции можно использовать эту фикстуру для взаимодействия с браузером. После завершения теста фикстура автоматически закрывает браузер`

#### ___В файле locators.py класс StellaBurgersLocators, который определяет набор локаторов:___

* `REGISTRATION_NAME_INPUT - поле Имя в форме регистрации`
* `REGISTRATION_EMAIL_INPUT - поле Email в форме регистрации `
* `REGISTRATION_PASSWORD_INPUT - поле Пароль в форме регистрации`
* `INCORRECT_PASSWORD_INSCRIPTION - "Неккоретный пароль"`
* `ENTER_ACCOUNT_BUTTON - кнопка "Войти в аккаунт"`
* `AUTH_EMAIL_INPUT - Поле ввода email при авторизации `
* `AUTH_PASSWORD_INPUT - Поел ввода password при авторизации `
* `HISTORY_ORDERS_BUTTON - кнопка "История заказов" в личном кабинете `
* `REGISTRATION_BUTTON - кнопка "Зарегистрироваться"`
* `LOGIN_BUTTON_IN_RESTORE_PASSWORD - кнопка "Войти" - восстановления пароля`
* `LOGIN_BUTTON_IN_REGISTRATION_FORM - кнопка "Войти" в форме регистрации `
* `CONFIRM_REGISTRATION_BUTTON - подтверждения регистрации `
* `PERSONAL_CABINET_BUTTON - Кнопка "Личный кабинет"`
* `RESTORE_PASSWORD_BUTTON - кнопка "Восстановить пароль"`
* `LOGIN_BUTTON - кнопка "Войти" при авторизации `
* `QUIT_PERSONAL_CABINET - кнопка "Выход" в личном кабинете`
* `CONSTRUCTOR_BUTTON - кнопка Конструктор `
* `LOGO_BUTTON - логотип сайта `
* `COLLECT_BURGER_TEXT - надпись "Соберите бургер"`
* `SAUCES_LOCATION_BUTTON - кнопка "Соусы" в конструкторе `
* `FILINGS_LOCATION_BUTTON - кнопка "Начинки" в конструкторе`
* `BUNS_LOCATION_BUTTON - кнопка "Булки" в конструкторе `
* `BUNS_PARRENT_CLASS - Класс выбранного раздела в Конструкторе`

#### ___В файле urls.py определяется список URL-адресов для использования в дальнейшем коде:___

* `MAIN_PAGE_URL — это основной URL веб-сайта`
* `REGISTRATION_SUCCES_URL — URL, на который переходит пользователь после успешной регистрации`
* `ENTER_PAGE_URL — страница входа в аккаунт`
* `PERSONAL_CABINET_PAGE_URL — личный кабинет пользователя`