import time

from selenium.common import WebDriverException, TimeoutException
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

    '''Локаторы товаров и их цен.'''
    phone_1 = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/a'
    phone_1_price = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/button/span/div[2]/span/span'
    phone_2 = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[3]/div/div/div[2]/div[3]/a'
    phone_2_price = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[3]/div/div/div[5]/div[2]/div/button/span/div[2]/span/span'
    phone_3 = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[4]/div/div/div[2]/div[3]/a'
    phone_3_price = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[4]/div/div/div[5]/div[2]/div/button/span/div[2]/span/span'

    '''Локаторы названия товара и его цены на странице товара для их сравнения со значениями в разделе товаров.'''
    product_page_name = '//div[@class="app-catalog-zf8fpo-TitleWrapper--StyledTitleWrapper e7n1imu0"]'
    product_page_price = '//*[@id="__next"]/div[1]/main/div/div[2]/div/div[4]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[2]/span/span'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода на страницу товара.'''
    main_word_product_page = '//*[@id="__next"]/div[1]/main/div/div[4]/div[2]/div/div[1]/div/section/div[1]/div/span'

    '''Локаторы кнопок добавления товара в корзину'''
    add_product_1_to_cart = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/div/div/button'
    add_product_2_to_cart = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[3]/div/div/div[5]/div[2]/div/div/button'
    add_product_3_to_cart = '//*[@id="__next"]/div[1]/main/section/div[4]/div/div[3]/section/div[2]/div[2]/div[4]/div/div/div[5]/div[2]/div/div/button'

    '''Локатор для перехода в корзину'''
    cart = '//*[@id="__next"]/div[1]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[4]/div/div/a/div/div'

    '''Локаторы названий и цен товаров в корзине.'''
    product_1_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[1]'
    product_2_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[2]'
    product_3_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[3]'
    product_1_cart_price = '(//span[@class="css-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[1]'
    product_2_cart_price = '//*[@id="__next"]/div[1]/main/div/div[2]/section/div[1]/div[2]/div/div/div/div[2]/div[7]/div/div[1]/div[2]/span/span'
    product_3_cart_price = '//*[@id="__next"]/div[1]/main/div/div[2]/section/div[1]/div[2]/div/div/div/div[3]/div[6]/div/div[1]/div[2]/span/span'

    '''Локатор суммарной цены'''
    product_in_cart_price = '//*[@id="__next"]/div[1]/main/div/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[4]/div/span'

    '''Локатор элемента страницы корзины.'''
    main_word_cart = '//span[@class="e1lzbfc40 e1a7a4n70 css-1f7sg44-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"]'

    '''Локатор кнопки закрытия всплывающего уведомления при добавлении товара в корзину'''
    continue_shopping = '//button[@class="eidfyie0 app-catalog-1uerbji-Button--StyledButton-Button--Button ekx3zbi0"]'


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

    def get_phone_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1)))

    def get_phone_1_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_1_price)))

    def get_phone_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_2)))

    def get_phone_2_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_2_price)))

    def get_phone_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_3)))

    def get_phone_3_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_3_price)))

    def get_product_page_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_page_name)))

    def get_product_1_cart_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_cart_name)))

    def get_product_2_cart_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_cart_name)))

    def get_product_3_cart_name(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_3_cart_name)))

    def get_product_page_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_page_price)))

    def get_product_1_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_1_cart_price)))

    def get_product_2_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_2_cart_price)))

    def get_product_3_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((By.XPATH, self.product_3_cart_price)))

    def get_product_in_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_in_cart_price)))

    def get_main_word_product_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_product_page)))

    def get_main_word_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_cart)))

    def get_add_product_1_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_1_to_cart)))

    def get_add_product_2_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_2_to_cart)))

    def get_add_product_3_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_product_3_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_continue_shopping(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_shopping)))


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
    def click_phone_1(self):
        self.get_phone_1().click()
        print("Click chosen phone")

    '''Добавление 1 товара в корзину.'''
    def click_add_product_1_to_cart(self):
        self.get_add_product_1_to_cart().click()
        print("Click add product 1 to cart")

    '''Добавление 2 товара в корзину.'''
    def click_add_product_2_to_cart(self):
        try:
            self.get_add_product_2_to_cart().click()
            print("Click add product 2 to cart")
        except (WebDriverException, TimeoutException):
            self.get_continue_shopping().click()
            self.get_add_product_2_to_cart().click()
            print("Click add product 2 to cart")


    '''Добавление 3 товара в корзину.'''
    def click_add_product_3_to_cart(self):
        try:
            self.get_add_product_3_to_cart().click()
            print("Click add product 3 to cart")
        except (WebDriverException, TimeoutException):
            self.get_continue_shopping().click()
            self.get_add_product_3_to_cart().click()
            print("Click add product 3 to cart")

    '''Клик по корзине.'''
    def click_cart(self):
        try:
            self.get_cart().click()
            print("Click cart")
        except (WebDriverException, TimeoutException):
            self.get_continue_shopping().click()
            self.get_cart().click()
            print("Click cart")

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
        value_product_1_name = self.get_phone_1().text
        value_product_1_price = self.get_phone_1_price().text
        self.click_phone_1()
        self.assert_product_name(value_product_1_name, self.get_product_page_name())
        self.assert_price(value_product_1_price, self.get_product_page_price())
        self.assert_main_word(self.get_main_word_product_page(), 'Описание')


    '''Фильтрация товаров и выбор 3 товаров.'''
    def filter_and_select_3_products(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/catalog/smartfony/APPLE/?ref=mainmenu")
        self.move_max_price_pointer(-60)
        self.click_available_for_delivery()
        self.click_for_sale()
        self.click_warranty()
        self.click_warranty_1_year()
        self.click_apply()
        value_product_1_name = self.get_phone_1().text
        value_product_1_price = self.get_phone_1_price().text
        value_product_2_name = self.get_phone_2().text
        value_product_2_price = self.get_phone_2_price().text
        value_product_3_name = self.get_phone_3().text
        value_product_3_price = self.get_phone_3_price().text
        self.click_add_product_1_to_cart()
        time.sleep(3)
        self.click_add_product_2_to_cart()
        time.sleep(3)
        self.click_add_product_3_to_cart()
        time.sleep(3)
        self.click_cart()
        self.assert_product_name(value_product_1_name, self.get_product_1_cart_name())
        self.assert_price(value_product_1_price, self.get_product_1_cart_price())
        self.assert_product_name(value_product_2_name, self.get_product_2_cart_name())
        self.assert_price(value_product_2_price, self.get_product_2_cart_price())
        self.assert_product_name(value_product_3_name, self.get_product_3_cart_name())
        self.assert_price(value_product_3_price, self.get_product_3_cart_price())
        self.assert_sum_price(value_product_1_price, value_product_2_price, value_product_3_price, self.get_product_in_cart_price() )
        self.assert_main_word(self.get_main_word_cart(), 'Корзина')

