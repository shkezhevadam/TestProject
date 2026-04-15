import datetime

class Base():

    def __init__(self, driver):
        self.driver = driver

    '''Method get current url'''
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Correct URL")

    """Method assert word"""
    def assert_main_word(self, word, result):
        value_word = word.text
        print(value_word)
        assert value_word == result
        print("Good main word value on new page")

    """Method assert product name"""
    def assert_product_name(self, name_1, name_2_object):
        try:
            print("Product name on previous page:" + name_1)
            name_2 = name_2_object.text
            print("Product name on current page:" + name_2)
            assert name_1 == name_2
            print("Product name is the same")
        except AssertionError:
            print("Name is different")

    """Method assert price"""
    def assert_price(self, price_1, price_2_object):
        print("Product price on previous page:" + price_1)
        price_2 = price_2_object.text
        print("Product price on current page:" + price_2)
        assert price_1 == price_2
        print("Price is the same")

    """Method screenshot"""
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot("C:\\Users\\Adam\\PyCharmProjects\\Citilink\\screenshots\\" + name_screenshot)
        print("Get a screenshot")