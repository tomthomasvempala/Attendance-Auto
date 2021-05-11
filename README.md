# Attendance-Auto
Automatically marks attendance on Moodle on command

## Requirements
You need python to run this.
You will also need to install Selenium Library

```
python -m pip install selenium
```
Ensure the version of chromedriver.exe is matching with the Chrome in your system. As of now, it is for Chrome 89

## Using the app
Clone the repository
```
git clone https://github.com/tomthomasvempala/Attendance-Auto.git
cd Attendance-Auto
```

To mark the attedance of ongoing period 
```
python attendance.py
```

To mark the attendance of a specific subject
```
python attendance.py <SUBJECT CODE>
```
The following are the subject codes:
DBMS, OS, COA, GT, HUT, HNR, MNR, OSL, DEL

