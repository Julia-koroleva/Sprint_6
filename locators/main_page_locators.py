import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTIONS = [
    (1, (By.ID, "accordion__heading-0")),
    (2, (By.ID, "accordion__heading-1")),
    (3, (By.ID, "accordion__heading-2")),
    (4, (By.ID, "accordion__heading-3")),
    (5, (By.ID, "accordion__heading-4")),
    (6, (By.ID, "accordion__heading-5")),
    (7, (By.ID, "accordion__heading-6")),
    (8, (By.ID, "accordion__heading-7"))
]
    ANSWERS = [
    (1, (By.ID, "accordion__panel-0")),
    (2, (By.ID, "accordion__panel-1")),
    (3, (By.ID, "accordion__panel-2")),
    (4, (By.ID, "accordion__panel-3")),
    (5, (By.ID, "accordion__panel-4")),
    (6, (By.ID, "accordion__panel-5")),
    (7, (By.ID, "accordion__panel-6")),
    (8, (By.ID, "accordion__panel-7"))
]

    # Текст "Вопросы о важном"
    main_questions = [By.XPATH, "//div[text()='Вопросы о важном']"]

    # Кнопка "Заказать" вверху  страницы
    button_up = [By.CLASS_NAME, "Button_Button__ra12g"]

    # Кнопка "Заказать" вверху  страницы
    button_down = [By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM"]

    # Логотип Яндекс на главной странице Яндекс.Самокат
    logo_yandex = [By.CLASS_NAME, "Header_Logo__23yGT"]

    # Логотип ДЗЭН на странице dzen.ru
    dzen_logo = [By.XPATH, "//path[@fill='#fff' and contains(@d, 'M24.667 13.788a') and contains(@d, 'v-.447z')]"]