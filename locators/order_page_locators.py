import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Форма "Для кого самокат"
    name = [By.XPATH, "//input[@placeholder='* Имя']"]
    surname = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    metro = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    next = [By.XPATH, "//button[text()='Далее']"]

    # Форма "Про аренду"
    date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    rental_period = [By.CLASS_NAME, "Dropdown-root"]
    black_samocat = [By.ID, "black"]
    gray_samocat = [By.ID, "grey"]
    message = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    order_button = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']"]
    back = [By.XPATH, "//button[text()='Назад']"]
    yes_button = [By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']"]
    order_made = [By.XPATH, "//div[contains(@class, 'Order_Modal')]//div[contains(text(), 'Заказ оформлен')]"]

    # Логотипы
    logo_samocat = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]