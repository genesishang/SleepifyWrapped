
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

        entireFile = csvfile.readlines()
        lenFile = len(entireFile)
        count = 0
        start = entireFile[1].split(',')[0]
        time = start.split(' ')
        day = time[0]
        
        #whole file
        while (count != lenFile):
            #per day
            while (dateRetrieve(entireFile[count]) == day):
                #per row
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
                    count+=1
        avgSleep(sleepHours, totalAverages)
        avgHR(heartRates, totalAverages)

    print(totalAverages)



#helper
def minToHrs(mins):
     return round(mins/60.0, 1)

#helper
#retrieve times from data as string, assuming MONTH/DAY/YR HR:MIN:SEC AM/PM format)
def timeRetrieve(column):
     splitColumn = column.split(' ')
     return str(splitColumn[1])

def dateRetrieve(column):
     splitColumn = column.split(' ')
     return str(splitColumn[0])

#helper
#convert hrs to sec
def hrsToMin(hrs):
    return hrs*60

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

     #grabbing start time numbers and grouping by hrs, min

     startTime_hrs = int(num_startTime[0])
     startTime_total = int(num_startTime[1]) #total in min

     #grabbing end time numbers and grouping by hrs, min
     endTime_hrs = int(num_endTime[0])
     endTime_total = int(num_endTime[1])

     startTime_total += hrsToMin(startTime_hrs)
     endTime_total += hrsToMin(endTime_hrs)
     
     totalTime = (endTime_total-startTime_total)

     totalTime = minToHrs(totalTime)
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
