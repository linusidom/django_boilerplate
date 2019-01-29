from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
import os
import time

class FunctionalTesting(StaticLiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
		staging_server = os.environ.get('STAGING_SERVER')
		if staging_server:
			self.live_server_url = 'http://'+staging_server

	def tearDown(self):
		self.browser.quit()

class TestSignupLoginSuccess(FunctionalTesting):
	def test_signup_login_success(self):

		user_login = 'newuser@newuser.com'
		user_password = 'adminadmin'

		self.browser.get(self.live_server_url+'/accounts/signup/')

		email = self.browser.find_element_by_id('id_email')
		email.send_keys(user_login)
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys(user_password)
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys(user_password)
		password2.send_keys(Keys.ENTER)
		time.sleep(1)

		username = self.browser.find_element_by_id('id_username')
		username.send_keys(user_login)
		password = self.browser.find_element_by_id('id_password')
		password.send_keys(user_password)
		password.send_keys(Keys.ENTER)
		time.sleep(1)
		
		a_hrefs = self.browser.find_elements_by_tag_name('a')
		links = [a_href.text for a_href in a_hrefs]
		self.assertIn('Account Detail', links)

class TestSignupFail(FunctionalTesting):
	def test_signup_wrong_password(self):

		user_login = 'newuser@newuser.com'
		user_password1 = 'adminadmin'
		user_password2 = 'admin'
		self.browser.get(self.live_server_url+'/accounts/signup/')

		email = self.browser.find_element_by_id('id_email')
		email.send_keys(user_login)
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys(user_password1)
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys(user_password2)
		password2.send_keys(Keys.ENTER)
		time.sleep(1)
		errors = self.browser.find_element_by_class_name('errorlist').text
		self.assertEqual('The two password fields didn\'t match.', errors)

	def test_signup_user_exists_already(self):

		user_login = 'newuser@newuser.com'
		user_password1 = 'adminadmin'
		user_password2 = 'adminadmin'
		self.browser.get(self.live_server_url+'/accounts/signup/')

		email = self.browser.find_element_by_id('id_email')
		email.send_keys(user_login)
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys(user_password1)
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys(user_password2)
		password2.send_keys(Keys.ENTER)
		time.sleep(1)
		self.browser.get(self.live_server_url+'/accounts/signup/')

		email = self.browser.find_element_by_id('id_email')
		email.send_keys(user_login)
		password1 = self.browser.find_element_by_id('id_password1')
		password1.send_keys(user_password1)
		password2 = self.browser.find_element_by_id('id_password2')
		password2.send_keys(user_password2)
		password2.send_keys(Keys.ENTER)
		time.sleep(1)
		errors = self.browser.find_element_by_tag_name('p').text
		self.assertEqual('e-mail already in use', errors)

class TestLoginFail(FunctionalTesting):
	def test_login_fail(self):
		
		user_login = 'newuser@newuser.com'
		user_password = 'adminadmin'

		self.browser.get(self.live_server_url+'/login/')

		username = self.browser.find_element_by_id('id_username')
		username.send_keys(user_login)
		password = self.browser.find_element_by_id('id_password')
		password.send_keys(user_password)
		password.send_keys(Keys.ENTER)
		time.sleep(1)
		errors = self.browser.find_element_by_class_name('errorlist').text
		self.assertEqual('Please enter a correct username and password. Note that both fields may be case-sensitive.', errors)