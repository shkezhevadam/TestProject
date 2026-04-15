from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Product_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    add_to_cart = '//button[@class="e1wjwlu80 eidfyie0 app-catalog-1srevuk-Button--StyledButton-Button--Button-ButtonWithIcon--StyledButtonWithIcon ekx3zbi0"]'
    cart = '//div[@data-meta-name="BasketButton"]'

    '''Локаторы названия товара и его цены на странице товара для их сравнения со значениями в корзине.'''
    product_page_name = '//div[@class="app-catalog-zf8fpo-TitleWrapper--StyledTitleWrapper e7n1imu0"]'
    product_page_price = '//*[@id="__next"]/div[1]/main/div/div[2]/div/div[4]/div/div[3]/div/div[1]/div[1]/div[1]/div/div[2]/span/span'

    '''Локаторы названия и цены товара в корзине (на странице корзины две цены, поэтому сравниваю вторую цену тоже).'''
    product_cart_name = '//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"]'
    product_cart_price = '//*[@id="__next"]/div[1]/main/div/div[2]/section/div[1]/div/div/div/div/div/div[6]/div/div[1]/div[2]/span'
    product_in_cart_price = '//*[@id="__next"]/div[1]/main/div/div[2]/section/div[2]/div/div[1]/div[1]/div[1]/div[4]/div/span/span'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода в корзину.'''
    main_word_cart_page = '//span[@class="e1lzbfc40 e1a7a4n70 css-1f7sg44-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"]'

    # Getters
    def get_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_product_page_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page_name)))

    def get_product_page_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_page_price)))

    def get_product_cart_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_cart_name)))

    def get_product_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_cart_price)))

    def get_product_in_cart_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_in_cart_price)))

    def get_main_word_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_cart_page)))

    # Actions
    '''Клик по "Добавить в корзину".'''
    def click_add_to_cart(self):
        self.get_add_to_cart().click()
        print("Click Add to cart")

    '''Клик по корзине.'''
    def click_cart(self):
        self.get_cart().click()
        print("Click Cart")

    # Methods(Steps)
    "Добавление товара в корзину и переход в корзину."
    def add_product_to_cart(self):
        self.get_current_url()
        self.assert_url("https://www.citilink.ru/product/smartfon-apple-iphone-17-a3520-256gb-chernyi-3g-4g-1sim-6-3-1206x2622-2143350/")
        value_product_name = self.get_product_page_name().text
        value_product_price = self.get_product_page_price().text
        self.click_add_to_cart()
        self.click_cart()
        self.assert_product_name(value_product_name, self.get_product_cart_name())
        self.assert_price(value_product_price, self.get_product_cart_price())
        self.assert_price(value_product_price, self.get_product_in_cart_price())
        self.assert_main_word(self.get_main_word_cart_page(), 'Корзина')
        # self.get_screenshot()