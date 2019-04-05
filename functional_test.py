import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
# browser.get('http://localhost:8000')
# 
# 
# assert 'To-Do' in browser.title
# 
# browser.quit()

class NewVisitorTest(unittest.TestCase):
    
    
    def setUp(self):
        self.browser = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
    
    def tearDown(self):

        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        self.browser.get('http://127.0.0.1:8000/')
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

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows),
            f"New to-do item did not appear in table,contents were:\n{table.text}"
        )

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('User peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)


        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')

        self.assertIn("1:Buy peacock feathers",[row.text for row in rows])
        self.assertIn("2:User peacock feathers to make a fly",
                        [row.text for row in rows] 
        )

        self.fail('Finish the test')



if __name__ == '__main__':
    unittest.main()
