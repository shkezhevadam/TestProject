from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base

from faker import Faker

from utilities.logger import Logger


class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout = '//button[@class="eidfyie0 css-187ljum-Button--StyledButton-Button--Button ekx3zbi0"]'
    authorization = '//button[@class="eidfyie0 css-aoyh1h-Button--StyledButton-Button--Button ekx3zbi0"]'
    phone_number = '//input[@inputmode="tel"]'
    button_get_code = '//button[@class="egtgumg0 css-1gzxr9m-Button--StyledButton-Button--Button-Button--StyledSendSmsButton ekx3zbi0"]'

    '''Локаторы ключевых слов при оформлении заказа.'''
    bonus_message = '//span[@class="e1lzbfc40 e1a7a4n70 css-12lpo70-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"]'
    login_authorization = '/html/body/div[3]/div/div/div/div/div/form/div/div/div[1]/div[1]/div'

    # Getters
    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    def get_bonus_message(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.bonus_message)))

    def get_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.authorization)))

    def get_login_authorization(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_authorization)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_button_get_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_get_code)))

    # Actions
    '''Клик по "Перейти к оформлению".'''
    def click_checkout(self):
        self.get_checkout().click()
        print("Click Сheckout")

    '''Клик по кнопке входа или регистрации.'''
    def click_authorization(self):
        self.get_authorization().click()
        print("Click Authorization")

    '''Вводим случайный номер'''
    def input_phone_number(self):
        fake = Faker()
        self.get_phone_number().send_keys(fake.numerify('##########'))
        print("Input Phone number")

    '''Клик по "Получить код".'''
    def click_get_sms_code(self):
        self.get_button_get_code().click()
        print("Click Get code")

    # Methods(Steps)
    def checkout_verification(self):
        Logger.add_start_step(method='checkout_verification')
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/order/")
        self.click_checkout()
        self.assert_main_word(self.get_bonus_message(), "Зарегистрируйтесь или войдите в свой аккаунт, чтобы оформить заказ и получить бонусы за покупку")
        self.click_authorization()
        self.assert_main_word(self.get_login_authorization(), "Вход\n/\nРегистрация")
        self.input_phone_number()
        self.click_get_sms_code()
        Logger.add_end_step(url=self.driver.current_url, method='checkout_verification')




