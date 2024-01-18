import csv
"""
Authors: Trisha Atluri, Genesis Hang, Josiame Uwumukiza
Consulted:
Date: 2024-01-18
Purpose: Upskill Final Project
"""
#main method to run all functions
import csv

def main(filename): 
    with open(filename) as csvfile:
        lineReader = csv.DictReader(csvfile)
        sleepHours = {"Awake": [], "Light/Core": [], "Deep": [], "REM": []}
        heartRates = {"Awake": [], "Light/Core": [], "Deep": [], "REM": []}
        totalAverages = {"Awake": [], "Light/Core": [], "Deep": [], "REM": []}
        for row in lineReader:
            if(row['Category'] == 'Light/Core'):
                sleepHours["Light/Core"].append(calculateSleepDuration(row['Start Time'], row['End Time']))
            if(row['Category'] == 'Deep'):
                sleepHours["Deep"].append(calculateSleepDuration(row['Start Time'], row['End Time']))
            if(row['Category'] == 'REM'):
                sleepHours["REM"].append(calculateSleepDuration(row['Start Time'], row['End Time']))
            if(row['Category'] == 'Awake'):
                sleepHours["Awake"].append(calculateSleepDuration(row['Start Time'], row['End Time']))
            getHR(row, heartRates)
        avgSleep(sleepHours, totalAverages)
        avgHR(heartRates, totalAverages)
    print(totalAverages)


#helper
#convert sec to hrs
def secToMins(secs):
     #rounds to hundredths place
     min = round(secs/60.0, 2)
     return min

#helper
def minToHrs(mins):
     return round(mins/60.0, 1)

#helper
#retrieve times from data as string, assuming MONTH/DAY/YR HR:MIN:SEC AM/PM format)
def timeRetrieve(column):
     splitColumn = column.split(' ')
     return str(splitColumn[2])

#helper
#convert hrs to sec
def hrsToSec(hrs):
    return hrs*3600

#helper
#convert min to sec():
def minToSec(min):
     return min*60

#helper for calculateSleepDuration, conversion 
def calculateSleepDifference(startT, endT):
     #grabbing startTime from file
     startTime = timeRetrieve(startT)
     startTime_total = 0

     #grabbing endTime from file
     endTime = timeRetrieve(endT)
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
     
     totalTime = (endTime_total-startTime_total)

     totalTime = secToMins(totalTime)

     return minToHrs(totalTime)

#holds hours of sleep per day in list,each day being a new index
def calculateSleepDuration(startTime, endTime):
    sleepTypeHrs = 0
    sleepTypeHrs += calculateSleepDifference(startTime, endTime)
    return sleepTypeHrs

#output of calculateSleepDuration, used in avgSleep()
#sleepHours = {Awake: [], Light/Core: [], Deep: [], REM: []}
#heartRates = {Awake: [], Light/Core: [], Deep: [], REM: []}

#output of avgSleep, this should be initialized in main
#totalAverages = {Awake: [], Light/Core: [], Deep: [], REM: []}

def getHR(row, heartRates): #arg is created in main by opening the file and reading it into a dictReader obj
    #loop through each row in csv
    heartRates[row["Category"]].append(row["Heart Rate"])
    #ID sleep category
    #add the heart rate to corresponding sleep category key in heartRates dict

def avgSleep(sleepHours, totalAverages):
    for key in sleepHours:
        total = 0
        for value in sleepHours[key]:
            total+= value
        avg = total/len(sleepHours[key])
        totalAverages[key].append(avg)
        
def avgHR(heartRates, totalAverages):
    for key in heartRates:
        total = 0
        for value in heartRates[key]:
            total+= value
        avg = total/len(heartRates[key])
        totalAverages[key].append(avg)
