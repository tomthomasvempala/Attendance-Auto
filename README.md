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
The following are the subject codes (CS 2023): </br>
<strong>DBMS, OS, COA, GT, HUT, HNR, MNR, OSL, DEL</strong>
</br>


For someone from different department or batch to use this, just modify the subject codes, moodle attendance page ids and timetable in data.py.
</br>
There's also a question in attendance.py asking your class. You might wanna edit that too if you're not CS. 

</br>
And you find this project helpful, please consider dropping a star ⭐ 😊
