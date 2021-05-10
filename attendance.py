from selenium import webdriver
import sys
import os.path
import getpass
import ctypes
from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriveManager

MessageBox = ctypes.windll.user32.MessageBoxW
subId = {
    'AFM': '9902',
    'DBMS': '10120',
    'OS': '10137',
    'COA': '10118',
    'GT': '10468',
    'OSL': '10080',
    'DEL': '10205',
    'HUT': '10042',
    'HNR': '11073',
    'MNR': '9902',
}
myemail = ""
mypasswword = ""
if os.path.exists('moodle_creds.txt'):
    f = open("moodle_creds.txt", "r")
    myemail = f.readline()
    mypasswword = f.readline()
else:
    print("Enter email: ")
    myemail = input()
    print("Enter password: ")
    mypasswword = getpass.getpass()
    f = open('moodle_creds.txt', 'w')
    f.write(myemail+'\n')
    f.write(mypasswword)
    print("Your email and password will be remembered. To change it, edit moodle_creds.txt\n")

options =Options()
options.headless =True
driver = webdriver.Chrome(options= options)
sub=""
if len(sys.argv)==1:
    print("Enter subject code: ")
    sub=input().upper()
else:
    sub = sys.argv[1].upper()
driver.get('http://moodle.mec.ac.in/mod/attendance/view.php?id=' +
           subId[sub])
username = driver.find_element_by_id('username')
username.send_keys(myemail.strip('\n'))
password = driver.find_element_by_id('password')
password.send_keys(mypasswword)
loginbtn = driver.find_element_by_id('loginbtn')
loginbtn.click()
item = driver.find_elements_by_xpath(
    "//a[contains(text(),'Submit attendance')]")
if item == []:
    MessageBox(None, 'No attendance found', 'Attendance', 0)
    print("No Attendance")

else:
    item[0].click()
    present = driver.find_element_by_xpath(
        "//span[contains(text(),'Present')]")
    present.click()
    submit = driver.find_element_by_id('id_submitbutton')
    submit.click()
    MessageBox(None, 'Attendance marked for '+ sub +'succefully', 'Attendance', 0)
