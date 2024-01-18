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

#helper for calculateSleepDuration, conversion 
def calculateSleepDifference(rowNum):
     #splitting data by ':' to get ints to convert accordingly
     startTime = str(row['Start Time'], ':')
     startTime_total = 0

     endTime = str(row['End Time'], ':')
     endTime_total = 0

     #endTime_total - startTime_total ... results in sec need to convert back for user readability
     totalTime = 0

     num_startTime = startTime.split(':')
     num_endTime = endTime.split(':')

     startTime_hrs = num_startTime[0]
     startTime_min = num_startTime[1]
     startTime_sec = num_startTime[2]

     endTime_hrs = num_endTime[0]
     endTime_min = num_endTime[1]
     endTime_sec = num_endTime[2]
    
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
     
    
#holds hours of sleep per day in list,each day being a new index
def calculateSleepDuration(sleepType):
    sleepSchedule = []
    sleepTypeHrs = 0
    if (row['Category'] == sleepType):
            sleepTypeHrs += calculateSleepDifference(sleepType)

