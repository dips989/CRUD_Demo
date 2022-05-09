

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# class Hosttest(LiveServerTestCase):
#     def testloginpage(self):
#         driver = webdriver.Chrome()

#         driver.get('http://127.0.0.1:8000/')
#         time.sleep(5)
#         assert "Hello, world!!!" in driver.title

class LoginFormTest(LiveServerTestCase):

            def testform(self):
                driver = webdriver.Chrome()

                driver.get('http://127.0.0.1:8000/')

                time.sleep(5)

                user_name = driver.find_element_by_class_name('email')
                user_pswd = driver.find_element_by_class_name('pswd')

                time.sleep(5)
                
                submit = driver.find_element_by_id('submit')

                user_name.send_keys('admin@gmail.com')
                user_pswd.send_keys('admin123')

                submit.send_keys(keys.RETURN)

                assert 'admin@gmail.com' in driver.page_source