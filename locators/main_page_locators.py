import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class MainPageLocators:

    # Локаторы вопросов на главной странице сайта "Яндекс.Самокат" в Разделе "Вопросы о важном"
    QUESTIONS = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]
    
    # Локаторы ответов на вопросы на главной странице сайта "Яндекс.Самокат" в Разделе "Вопросы о важном"
    ANSWERS = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
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
    dzen_logo = [By.XPATH, "//a[contains(@href, 'dzen.ru')]"]