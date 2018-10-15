from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('C:\Personal\HTML-CSS\Python\chromedriver.exe')

    def test_search_in_python(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)
        elem = driver.find_element_by_name('q')
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)
        assert 'No Results Found' not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()