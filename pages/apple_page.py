from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Apple_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    '''Локаторы для фильтрации товаров.'''
    max_price_pointer = '//div[@class="rc-slider-handle rc-slider-handle-2"]'
    available_for_delivery = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div[3]/div/label/span[1]'
    for_sale = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[4]/div[2]/div/div/div/div/div/div[1]/div/label/span[1]'
    warranty = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[21]/div[1]/div/span[1]'
    warranty_1_year = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[1]/div/div/div/div/div/div/div/div[2]/div[2]/div[21]/div[2]/div/div/div/div/div/div/div/label/span[1]'
    apply = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[1]/div[1]/div/div/div/div/div/div/div[2]/div[2]/div[23]/button[1]/span'
    phone = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/a'
    phone_price = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[2]/div/div/div[5]/div[2]/div/button/span/div[2]/span/span'

    '''Локаторы названия товара и его цены на странице товара для их сравнения со значениями в разделе товаров.'''
    product_page_name = '//div[@class="app-catalog-zf8fpo-TitleWrapper--StyledTitleWrapper e7n1imu0"]'
    product_page_price = '//*[@id="__next"]/div[1]/main/div/div[2]/div/div[4]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[2]/span/span'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода на страницу товара.'''
    main_word_product_page = '//*[@id="__next"]/div[1]/main/div/div[4]/div[2]/div/div[1]/div/section/div[1]/div/span'


    # Getters
    def get_max_price_pointer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.max_price_pointer)))

    def get_available_for_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.available_for_delivery)))

    def get_for_sale(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_sale)))

    def get_warranty(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.warranty)))

    def get_warranty_1_year(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.warranty_1_year)))

    def get_apply(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apply)))

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
    '''Перемещение указателя максимальной цены.'''
    def move_max_price_pointer(self, x_offset_value):
        action = ActionChains(self.driver)
        action.click_and_hold(self.get_max_price_pointer()).move_by_offset(x_offset_value, 0).release().perform()
        print("Move Max price pointer")

    '''Клик по "Доступен для доставки".'''
    def click_available_for_delivery(self):
        self.get_available_for_delivery().click()
        print("Click Available for delivery")

    '''Клик по "Товары по акции".'''
    def click_for_sale(self):
        self.get_for_sale().click()
        print("Click Expand all sizes")

    '''Клик по "Гарантия".'''
    def click_warranty(self):
        self.driver.execute_script("window.scrollTo(0, 3000)")
        self.get_warranty().click()
        print("Click warranty")

    '''Клик по "1 год".'''
    def click_warranty_1_year(self):
        self.get_warranty_1_year().click()
        print("Click warranty 1 year")

    '''Клик по "Применить выбранное".'''
    def click_apply(self):
        self.get_apply().click()
        print("Click apply")

    '''Клик по названию выбранного товара.'''
    def click_phone(self):
        self.get_phone().click()
        print("Click chosen phone")

    # Methods(Steps)
    '''Фильтрация товаров и выбор товара.'''
    def filter_and_select_product(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/catalog/smartfony/APPLE/?ref=mainmenu")
        self.move_max_price_pointer(-60)
        self.click_available_for_delivery()
        self.click_for_sale()
        self.click_warranty()
        self.click_warranty_1_year()
        self.click_apply()
        value_product_name = self.get_phone().text
        value_product_price = self.get_phone_price().text
        self.click_phone()
        self.assert_product_name(value_product_name, self.get_product_page_name())
        self.assert_price(value_product_price, self.get_product_page_price())
        self.assert_main_word(self.get_main_word_product_page(), 'Описание')

