# Attendance-Auto
Automatically marks attendance on Moodle on command. Run a one line command, and sit back, relax.
Club it with a batch file and boom, you can schedule it with Task Scheduler on Windows 10.

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

