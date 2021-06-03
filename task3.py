from selenium import webdriver
from selenium.webdriver import ActionChains
import unittest


class UITestingMetricConversion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver.get("https://www.metric-conversions.org/")
        self.temperatureButton = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[1]")
        self.lengthButton = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[3]")
        self.weightButton = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/a[2]")
        self.driver.implicitly_wait(10)

    def searchingElementByXpath(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        attempts = 0

        while not element.is_enabled():
            element = self.driver.find_element_by_xpath(xpath)
            assert ++attempts <= 10, "cannot find element"

        return element

    def setupTest(self, right_answer, xpath):
        btn_to_conv = self.searchingElementByXpath(xpath)
        btn_to_conv.click()

        input_xpath = "/html/body/div[1]/div[1]/section[1]/form/input[1]"
        inp = self.searchingElementByXpath(input_xpath)

        inp.send_keys('12')
        inp.submit()

        mobile_ans = self.driver.find_element_by_id("mobileAnswer")
        ans = self.driver.find_element_by_id("answer")

        assert ans.text == right_answer or mobile_ans.text == right_answer, \
            "mobile_ans = {0}\nans = {1}".format(mobile_ans.text, ans.text)

    def test_CelsiusToFharenheit(self):
        self.temperatureButton.click()
        cel_to_fhar_btn_xpath = "/html/body/div[1]/div[3]/ol/li[1]/a"
        self.setupTest("12°C= 53.60000°F", cel_to_fhar_btn_xpath)

    def test_meterToFeet(self):
        self.lengthButton.click()
        meter_to_feet_btn_xpath = "/html/body/div[1]/div[3]/ol/li[1]/a"
        self.setupTest("12m= 39ft 4.440946in", meter_to_feet_btn_xpath)

    def test_ouncesToGrams(self):
        self.weightButton.click()
        ounces_to_gram_btn_xpath = "/html/body/div[1]/div[3]/ol/li[5]/a"
        self.setupTest("12oz= 340.1943g", ounces_to_gram_btn_xpath)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    UITestingMetricConversion.main()
