from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Search_Result_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    phone = '//*[@id="__next"]/div[1]/main/div/div/div[2]/section/div[2]/div[2]/div/div/div/div[2]/div[3]/a'
    phone_price = '//span[@class="app-catalog-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"]'

    '''Локаторы названия товара и его цены на странице товара для их сравнения со значениями в разделе товаров.'''
    product_page_name = '//div[@class="app-catalog-zf8fpo-TitleWrapper--StyledTitleWrapper e7n1imu0"]'
    product_page_price = '//*[@id="__next"]/div[1]/main/div/div[2]/div/div[4]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[2]/span/span'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода на страницу товара.'''
    main_word_product_page = '//*[@id="__next"]/div[1]/main/div/div[4]/div[2]/div/div[1]/div/section/div[1]/div/span'

    #Getters
    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_phone_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_price)))

    def get_product_page_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_page_name)))

    def get_product_page_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_page_price)))

    def get_main_word_product_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_product_page)))

    # Actions
    '''Клик по названию выбранного товара.'''
    def click_phone(self):
        self.get_phone().click()
        print("Click chosen phone")

    # Methods(Steps)
    '''Переход на страницу выбранного товара.'''
    def select_product(self):
        Logger.add_start_step(method='select_product')
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/search/?text=6.3%22+%D0%A1%D0%BC%D0%B0%D1%80%D1%82%D1%84%D0%BE%D0%BD+Apple+iPhone+17+256Gb%2C+A3520%2C+%D1%87%D0%B5%D1%80%D0%BD%D1%8B%D0%B9")
        value_product_name = self.get_phone().text
        value_product_price = self.get_phone_price().text
        self.click_phone()
        self.assert_product_name(value_product_name, self.get_product_page_name())
        self.assert_price(value_product_price, self.get_product_page_price())
        self.assert_main_word(self.get_main_word_product_page(), 'Описание')
        Logger.add_end_step(url=self.driver.current_url, method='select_product')