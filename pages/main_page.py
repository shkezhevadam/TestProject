import allure

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger


class Main_Page(Base):

    url = "https://www.citilink.ru/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    catalog = '//a[@href="/catalog/"]'
    phones_tablets_headphones = '/html/body/div[3]/div/div/div/div/div/div[5]/div/div/div/div/div[1]/div/div[1]/div/a[3]/div/span'
    apple_phones = '(//span[@class="em95myw0 app-catalog-1wyeo8j-GroupItem--StyledSubCategoryGroupItem-GroupItem--GroupItemWithStyles eoq77kn0"])[1]'
    search_bar = '//input[@placeholder="Поиск по товарам"]'
    search_button = '(//button[@class="app-catalog-13hgilf-BaseButton--BaseButton-components--Button-IconButton--StyledIconButton e1e3s3bk0"])[2]'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после перехода в раздел товаров.'''
    main_word = '//div[@class="app-catalog-1d0tddh e192la1o0"]'

    '''Локатор элемента следующей страницы для сравнения с ожидаемым значением после поиска товара.'''
    main_word_search = '//h1[@class="erx657h0 eyw7vua0 app-catalog-1mjne82-StyledTypography--getTypographyStyle-composeBreakpointsStyles--arrayOfStylesByBreakpoints-StyledHeading--getHeadingStyle-Heading--StyledHeadingComponent e1d9wgme0"]'

    #Getters
    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog)))

    def get_phones_tablets_headphones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones_tablets_headphones)))

    def get_apple_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.apple_phones)))

    def get_search_bar(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_bar)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_main_word_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word_search)))

    #Actions

    '''Кликаем по каталогу.'''
    def click_catalog(self):
        self.get_catalog().click()
        print("Click catalog button")

    '''Наводимся на поле "Бег, ходьба".'''
    def move_to_phones_tablets_headphones(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.get_phones_tablets_headphones()).perform()
        print("Move to Running, walking")

    '''Кликаем на кнопку "Асфальт" в разделе "Мужская обувь".'''
    def click_apple_phones(self):
        self.get_apple_phones().click()
        print("Click Man's Asphalt")

    '''Кликаем по строке поиска.'''
    def click_search_bar(self):
        self.get_search_bar().click()
        print("Click search bar")

    '''Вводим название товара'''
    def input_product_name(self, product_name):
        self.get_search_bar().send_keys(product_name)
        print("Input product name")

    '''Кликаем по кнопке поиска'''
    def click_search_button(self):
        self.get_search_button().click()
        print("Click search button")


    #Methods(Steps)
    '''Выбор раздела товаров'''
    def select_product_section(self):
        with allure.step('Select product section'):
            Logger.add_start_step(method='select_product_section')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_catalog()
            self.move_to_phones_tablets_headphones()
            self.click_apple_phones()
            self.assert_main_word(self.get_main_word(), "Apple iPhone")
            self.assert_url("https://www.citilink.ru/catalog/smartfony/APPLE/?ref=mainmenu")
            Logger.add_end_step(url=self.driver.current_url, method='select_product_section')


    '''Поиск по названию товара'''
    def search_for_product(self):
        with allure.step("Search for product"):
            Logger.add_start_step(method='search_for_product')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_search_bar()
            self.input_product_name('6.3" Смартфон Apple iPhone 17 256Gb, A3520, черный')
            self.click_search_button()
            self.assert_main_word(self.get_main_word_search(), 'Результаты для «6.3" Смартфон Apple iPhone 17 256Gb, A3520, черный»')
            Logger.add_end_step(url=self.driver.current_url, method='search_for_product')









