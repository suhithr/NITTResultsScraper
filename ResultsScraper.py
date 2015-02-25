from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
lower = input("Enter the first roll number : ")
upper = input("Enter the last roll number : ")
print 'The results will be scraped from ' +str(lower)+ ' to ' +str(upper)
driver = webdriver.Firefox()
driver.get("http://www.nitt.edu/prm/nitreg/ShowRes.aspx")
#selects the text box form wherein roll number is entered
form = driver.find_element_by_name("TextBox1")


def check_exists():
	try:
		driver.find_element_by_id('LblName')
	except NoSuchElementException:
		return False
	return True

def assign(rollno):
	form = driver.find_element_by_name("TextBox1")
	form.send_keys(str(rollno))
	form.send_keys(Keys.RETURN)
	driver.implicitly_wait(3)

	if check_exists() is True:
		name = driver.find_element_by_id('LblName')
		gpa = driver.find_element_by_id('LblGPA')
		print str(rollno) + '-> Name: '+str(name.text)+' ->GPA: '+str(gpa.text)

	driver.get("http://www.nitt.edu/prm/nitreg/ShowRes.aspx")
	#selects the text box form wherein roll number is entered
	form = driver.find_element_by_name("TextBox1")

for r in range(lower, upper + 1):
	assign(r)
driver.close()
