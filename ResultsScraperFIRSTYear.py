from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions
from selenium.common.exceptions import NoSuchElementException
print "Architecture, Chemical, Civil, CSE, ECE, EEE, ICE, Mechanical, MME, Production"
branch = raw_input("Enter the branch to fetch the results from: ")
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

if branch == 'Architecture':
	for r in range(1,52):
		rollno = 101114000 + r
		assign(rollno)

if branch == 'Chemical':
	for r in range(1,72):
		rollno = 102114000 + r
		assign(rollno)
if branch == 'Civil':
	for r in range(1,104):
		rollno = 103114000 + r
		assign(rollno)
if branch == 'CSE':
	for r in range(1,106):
		rollno = 106114000 + r
		assign(rollno)
if branch == 'ECE':
	for r in range(1,106):
		rollno = 108114000 + r
		assign(rollno)
if branch == 'EEE':
	for r in range(1,105):
		rollno = 107114000 + r
		assign(rollno)
if branch == 'ICE':
	for r in range(1,99):
		rollno = 110114000 + r
		assign(rollno)
if branch == 'Mechanical':
	for r in range(1,109):
		rollno = 111114000 + r
		assign(rollno)
if branch == 'MME':
	for r in range(1,66):
		rollno = 112114000 + r
		assign(rollno)
if branch == 'Production':
	for r in range(1,102):
		rollno = 114114000 + r
		assign(rollno)
driver.close()
