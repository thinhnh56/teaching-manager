from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class viewsTest(LiveServerTestCase):
    fixtures = ['user.json']
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(5)

    def tearDown(self):
        self.browser.quit()
    
    def test_can_open_login_site(self):
        # An user open web browser and can open the login site's url
        self.browser.get(self.live_server_url)
        
        # He sees 'login site for non-staff user'
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Enter your username and password to login', body.text)
        
        # He looks for username field
        username_field = self.browser.find_element_by_name('username')
        # He looks for password field
        password_field = self.browser.find_element_by_name('password')
        
        # He types in his username and password then hit Enter
        username_field.send_keys('abcd')
        password_field.send_keys('12')
        password_field.send_keys(Keys.RETURN)
        
        # He failed to login
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Wrong username/password', body.text)
        
        # He looks for username field and clears it
        username_field = self.browser.find_element_by_name('username')
        username_field.clear()
        # He looks for password field and clears it
        password_field = self.browser.find_element_by_name('password')
        password_field.clear()
        
        # He types in his username and password again then hit Enter
        username_field.send_keys('abcd')
        password_field.send_keys('1234')
        password_field.send_keys(Keys.RETURN)
        
        # This time he logged in successfully
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('You have logged in successfully', body.text)
        