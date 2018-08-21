from selenium import webdriver
import unittest
from selenium.webdriver.common import 


def main():

	dr = webdriver.Chrome()
	dr.get('https://testnew.cloudcubic.net/login.aspx')
	dr.implicitly_wait(10)






if __name__ == '__main__':
	mian()