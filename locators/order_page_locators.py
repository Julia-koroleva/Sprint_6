import sys 
sys.path.append('..')
from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Поле для ввода имени на форме "Для кого самокат?"
    name = [By.XPATH, "//input[@wfd-id='id7']"]
    
    # Поле для ввода фамилии на форме "Для кого самокат?"
    surname = [By.XPATH, "//input[@wfd-id='id8']"]

    # Поле для ввода адреса на форме "Для кого самокат?"
    address = [By.XPATH, "//input[@wfd-id='id9']"]

    # Поле для ввода станции метро на форме "Для кого самокат?"
    metro = [By.XPATH, "//input[@wfd-id='id10']"]

    # Поле для ввода телефона на форме "Для кого самокат?"
    phone =  [By.XPATH, "//input[@wfd-id='id11']"]

    # Кнопка "Далее" на форме "Для кого самокат?"
    next = [By.XPATH, "//button[text()='Далее']"]

    # Поле для вводы даты "Когда привезти самокат" на форме "Про аренду"
    date = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]

    # Поле для ввода срока аренды на форме "Про аренду"
    rental_period = [By.CLASS_NAME, "Dropdown-placeholder is-selected"]
    
    # Чек-бокс для ввода цвета самоката "Черный жемчуг" на форме "Про аренду" 
    black_samocat = [By.ID, "black"]

    # Чек-бокс для ввода цвета самоката "Серая безысходность" на форме "Про аренду" 
    gray_samocal = [By.ID, "gray"]

    # Кнопка "Заказать" на форме "Про аренду" 
    order = [By.XPATH, "//button[text()='Заказать']"]
    
    # Логотип Яндекс.Самокат 
    logo_yandex = [By.CLASS_NAME, "Header_Logo__23yGT"]

    # Кнопака "Назад" на форме заказа самоката
    back = [By.XPATH, "//button[text()='Назад']"]

    # Кнопака "Да" на форме заказа самоката
    yes_button = [By.XPATH, "//button[text()='Да']"]

    # Извещение о создании заказа
    order_made = [By.LINK_TEXT, "Заказ оформлен"]

   # Логотип Самокат на странице заказа самоката Яндекс.Самокат
    logo_samocat = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]