import time
import allure
from selenium.common import WebDriverException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Apple_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    '''Локаторы для фильтрации товаров.'''
    max_price_pointer = '//div[@class="rc-slider-handle rc-slider-handle-2"]'
    available_for_delivery = '(//span[@class="e9gxmdn0 app-catalog-2s5ps0-Wrapper--StyledWrapper-Checkbox--StyledCheckboxComponent enxkrel0"])[2]'
    for_sale = '(//span[@class="e9gxmdn0 app-catalog-2s5ps0-Wrapper--StyledWrapper-Checkbox--StyledCheckboxComponent enxkrel0"])[2]'
    warranty = '(//span[@class="app-catalog-k1irjw e1o626c90"])[18]'
    warranty_1_year = '(//span[@class="e9gxmdn0 app-catalog-2s5ps0-Wrapper--StyledWrapper-Checkbox--StyledCheckboxComponent enxkrel0"])[43]'
    apply = '//button[@class="eidfyie0 app-catalog-1bflktt-Button--StyledButton-Button--Button ekx3zbi0"]'

    '''Локаторы товаров и их цен.'''
    phone_1 = '(//div[@class="app-catalog-1p7hp34-Flex--StyledFlex-Name--StyledName ezwjdcp0"])[1]'
    phone_1_price = '(//span[@class="eyylnuu0 e1vrd3w50 e1a7a4n70 app-catalog-1mc2zba-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-Wrapper--StyledWrapper-Price--StyledPrice e1d9wgme0"])[1]'
    phone_2 = '(//div[@class="app-catalog-1p7hp34-Flex--StyledFlex-Name--StyledName ezwjdcp0"])[2]'
    phone_2_price = '(//span[@class="eyylnuu0 e1vrd3w50 e1a7a4n70 app-catalog-1mc2zba-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-Wrapper--StyledWrapper-Price--StyledPrice e1d9wgme0"])[2]'
    phone_3 = '(//div[@class="app-catalog-1p7hp34-Flex--StyledFlex-Name--StyledName ezwjdcp0"])[3]'
    phone_3_price = '(//span[@class="eyylnuu0 e1vrd3w50 e1a7a4n70 app-catalog-1mc2zba-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent-Wrapper--StyledWrapper-Price--StyledPrice e1d9wgme0"])[3]'

    '''Локаторы названия товара и его цены на странице товара для их сравнения со значениями в разделе товаров.'''
    product_page_name = '//div[@class="app-catalog-zf8fpo-TitleWrapper--StyledTitleWrapper e7n1imu0"]'
    product_page_price = '(//span[@class="app-catalog-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[1]'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода на страницу товара.'''
    main_word_product_page = '//div[@class="app-catalog-1or1r4y-StyledTextWrapper--StyledTextWrapper eiw2hmd0"]'

    '''Локаторы кнопок добавления товара в корзину'''
    add_product_1_to_cart = '(//button[@class="eidfyie0 app-catalog-10s4dr8-Button--StyledButton-Button--Button ekx3zbi0"])[1]'
    add_product_2_to_cart = '(//button[@class="eidfyie0 app-catalog-10s4dr8-Button--StyledButton-Button--Button ekx3zbi0"])[1]'
    add_product_3_to_cart = '(//button[@class="eidfyie0 app-catalog-10s4dr8-Button--StyledButton-Button--Button ekx3zbi0"])[1]'

    '''Локатор для перехода в корзину'''
    cart = '//div[@data-meta-name="BasketButton"]'

    '''Локаторы названий и цен товаров в корзине.'''
    product_1_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[1]'
    product_2_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[2]'
    product_3_cart_name = '(//span[@class="e1lzbfc40 e1a7a4n70 css-t13lc6-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledText--getTextStyle-Text--StyledTextComponent e1d9wgme0"])[3]'
    product_1_cart_price = '(//span[@class="css-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[1]'
    product_2_cart_price = '(//span[@class="css-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[7]'
    product_3_cart_price = '(//span[@class="css-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[13]'

    '''Локатор суммарной цены'''
    product_in_cart_price = '(//span[@class="css-1qcsymx-MetaWrapper--StyledMetaWrapper e1l3zmw0"])[19]'

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
        with allure.step("Filter and select product"):
            Logger.add_start_step(method='filter_and_select_product')
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
            Logger.add_end_step(url=self.driver.current_url, method='filter_and_select_product')


    '''Фильтрация товаров и выбор 3 товаров.'''
    def filter_and_select_3_products(self):
        with allure.step("Filter and select 3 products"):
            Logger.add_start_step(method='filter_and_select_3_products')
            self.get_current_url()
            self.assert_url("https://www.citilink.ru/catalog/smartfony/APPLE/?ref=mainmenu")
            self.move_max_price_pointer(-60)
            self.click_available_for_delivery()
            self.click_for_sale()
            self.click_warranty()
            self.click_warranty_1_year()
            self.click_apply()
            self.click_add_product_1_to_cart()
            time.sleep(3)
            self.click_add_product_2_to_cart()
            time.sleep(3)
            self.click_add_product_3_to_cart()
            time.sleep(3)
            self.click_cart()
            value_product_1_price = self.get_product_1_cart_price().text
            value_product_2_price = self.get_product_2_cart_price().text
            value_product_3_price = self.get_product_3_cart_price().text
            self.assert_sum_price(value_product_1_price, value_product_2_price, value_product_3_price, self.get_product_in_cart_price() )
            self.assert_main_word(self.get_main_word_cart(), 'Корзина')
            Logger.add_end_step(url=self.driver.current_url, method='filter_and_select_3_products')

