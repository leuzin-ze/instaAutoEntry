from selenium import webdriver
from time import sleep

class InstaBot:
	def __init__(self, username, pw):
		self.driver = webdriver.Chrome("C:\\webdrivers\\chromedriver.exe")
		self.username = username
		self.driver.get('https://instagram.com')
		sleep(2)
		self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)
		self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(pw)
		self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
		sleep(4)
		self.driver.find_element_by_xpath("//button[contains(text(), 'Agora não')]").click()
		sleep(4)
		
	def get_unfollowers(self):
		self.driver.find_element_by_xpath("//a[contains(@href, '/{}')]".format(self.username)).click()

my_Bot = InstaBot('', '')
my_Bot.get_unfollowers()