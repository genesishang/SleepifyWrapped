"""
Authors: Trisha Atluri, Genesis Hang, Josiame Uwumukiza
Consulted:
Date: 2024-01-18
Purpose: Upskill Final Project
"""
#main method to run all functions
def main(filename): 
    with open(filename) as csvfile:
        lineReader = csv.DictReader(csvfile)
        for row in lineReader:
        #    list.append(row['company'])
             calculateSleepDuration('Light/Core')
    csvfile.close()
    return list

#helper
#retrieve times from data as string, assuming MONTH/DAY/YR HR:MIN:SEC AM/PM format)
def timeRetrieve(columnName):
     splitColumn = row[columnName]
     return str(splitColumn[1])

#helper
#convert hrs to sec
def hrsToSec(hrs):
    sec = hrs*3600
    return sec

#helper
#convert min to sec():
def minToSec(min):
     sec = min*60
     return sec

#helper for calculateSleepDuration, conversion 
def calculateSleepDifference(rowNum):
     #grabbing startTime from file
     startTime = timeRetrieve('Start Time')
     startTime_total = 0

     #grabbing endTime from file
     endTime = timeRetrieve('End Time')
     endTime_total = 0

     #endTime_total - startTime_total ... results in sec need to convert back for user readability
     totalTime = 0

     #splitting data by ':' to get ints to convert accordingly
     num_startTime = startTime.split(':')
     num_endTime = endTime.split(':')

     #grabbing start time numbers and grouping by hrs, min, sec

     startTime_hrs = int(num_startTime[0])
     startTime_min = int(num_startTime[1])
     startTime_total = int(num_startTime[2])

     #grabbing end time numbers and grouping by hrs, min, sec
     endTime_hrs = int(num_endTime[0])
     endTime_min = int(num_endTime[1])
     endTime_total = int(num_endTime[2])

     startTime_total += hrsToSec(startTime_hrs)
     startTime_total += minToSec(startTime_min)

     endTime_total += hrsToSec(endTime_hrs)
     endTime_total += minToSec(endTime_min)
     
#holds hours of sleep per day in list,each day being a new index
def calculateSleepDuration(sleepType):
    sleepSchedule = []
    sleepTypeHrs = 0
    if (row['Category'] == sleepType):
            sleepTypeHrs += calculateSleepDifference(sleepType)

