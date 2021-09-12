import time
import unittest

from selenium import webdriver


class TestMail(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.126.com/')

    def test_login(self):
        time.sleep(2)
        self.driver.switch_to.frame(2)
        print('haha')
        self.driver.find_element_by_id('confirm')
        print('hehe')
        time.sleep(2)
        # self.username = self.driver.find_element_by_name('email')
        print(self.driver.find_element_by_id('cnt-box').get_attribute('class'))
        self.username = self.driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/form/div/div[1]/div[2]/input')
        self.username.send_keys('yuanyongxian2021')
        self.password = self.driver.find_element_by_id('pwdtext')
        self.password.send_keys('Qwert1234')
        self.driver.find_element_by_id('auto-id-1631189778096').click()

    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
