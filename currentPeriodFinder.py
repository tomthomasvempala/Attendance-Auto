import datetime as dt

weekDay=dt.datetime.today().weekday()
currTime=dt.datetime.now().time()


timeTable = [
  ["DBMS", "DBMS", "GT", "HUT", "OSL"],
  ["COA", "OS", "DBMS", "DBMS", "DEL"],
  ["HNRS", "COA", "GT", "OS", "MNR"],
  ["COA", "OS", "GT", "HNRS", "MNR"],
  ["OS", "COA", "GT", "HUT", "HNRS"],
]


def isNowInTimePeriod(startTime, endTime, nowTime): 
    if startTime < endTime: 
        return nowTime >= startTime and nowTime <= endTime 
    else: 
        #Over midnight: 
        return nowTime >= startTime or nowTime <= endTime 

#normal example: 
def findCurrPeriod():
	if weekDay==4:
		if(isNowInTimePeriod(dt.time(8,30), dt.time(9,10), currTime)):
			return 0
		elif(isNowInTimePeriod(dt.time(9,10), dt.time(10,00), currTime)):
			return 1
		elif(isNowInTimePeriod(dt.time(10,00), dt.time(10,50), currTime)):
			return 2
		elif(isNowInTimePeriod(dt.time(10,50), dt.time(11,40), currTime)):
			return 3
		elif(isNowInTimePeriod(dt.time(11,40), dt.time(16,00), currTime)):
			return 4
		else :
			return 0
	else:
		if(isNowInTimePeriod(dt.time(8,30), dt.time(9,30), currTime)):
			return 0
		elif(isNowInTimePeriod(dt.time(9,30), dt.time(10,30), currTime)):
			return 1
		elif(isNowInTimePeriod(dt.time(10,30), dt.time(11,30), currTime)):
			return 2
		elif(isNowInTimePeriod(dt.time(11,30), dt.time(12,30), currTime)):
			return 3
		elif(isNowInTimePeriod(dt.time(12,30), dt.time(15,30), currTime)):
			return 4
		else :
			return 0
	

def getCurrPeriod():
	currPeriodNum=findCurrPeriod()
	currPeriod=timeTable[weekDay][currPeriodNum]
	return currPeriod

# print(currPeriod)