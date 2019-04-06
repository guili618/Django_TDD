import time
import unittest
######################
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.excetions import WebDriverException


# browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# browser.get('http://localhost:8000')
# 
# 
# assert 'To-Do' in browser.title
# 
# browser.quit()
MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):
    
    
    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text,[row.text for row in rows])
    
    def wait_for_row_in_list_table(self,row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text,[row.text for row in rows])
                return 
            except (AssertionError,WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get(self.live_server_url)
        self.assertIn('To-Do',self.browser.title)

        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')

        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        #table = self.browser.find_element_by_id('id_list_table')
        #rows = table.find_elements_by_tag_name('tr')
#
        #self.assertTrue(
            #any(row.text == '1:Buy peacock feathers' for row in rows),
            #f"New to-do item did not appear in table,contents were:\n{table.text}"
        #)

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('User peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
# 
        # self.assertIn("1:Buy peacock feathers",[row.text for row in rows])
        # self.assertIn("2:User peacock feathers to make a fly",
                        # [row.text for row in rows] 
        # )
        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        self.wait_for_row_in_list_table('2: User peacock feathers to make a fly')

        self.fail('Finish the test')



# if __name__ == '__main__':
    # unittest.main()
