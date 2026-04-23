import allure

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from pages.main_page import Main_Page
from pages.apple_page import Apple_Page
from pages.product_page import Product_Page
from pages.cart_page import Cart_Page

from conftest import set_group
from conftest import set_up


@allure.description("Test buy product")
def test_buy_product(set_group, set_up):

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--guest")

    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    mp = Main_Page(driver)
    mp.select_product_section()

    ap = Apple_Page(driver)
    ap.filter_and_select_product()

    pp = Product_Page(driver)
    pp.add_product_to_cart()

    cp = Cart_Page(driver)
    cp.checkout_verification()


