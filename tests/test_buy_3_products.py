import allure
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

from pages.main_page import Main_Page
from pages.apple_page import Apple_Page
from pages.cart_page import Cart_Page

from conftest import set_group
from conftest import set_up

@allure.description("Test buy 3 products")
def test_buy_3_products(set_group, set_up):

    options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # options.add_argument("--guest")

    g = Service()
    driver = webdriver.Chrome(options=options, service=g)

    mp = Main_Page(driver)
    mp.select_product_section()

    ap = Apple_Page(driver)
    ap.filter_and_select_3_products()

    cp = Cart_Page(driver)
    cp.checkout_verification()

