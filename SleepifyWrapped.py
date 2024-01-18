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
     


#holds hours of sleep per day in list,each day being a new index
def calculateSleepDuration(sleepType):
    sleepSchedule = []
    sleepTypeHrs = 0
    if (row['Category'] == sleepType):
            sleepTypeHrs = calculateSleepDifference(sleepType)

#output of calculateSleepDuration, used in avgSleep()
sleepHours = {Awake: [], Light/Core: [], Deep: [], REM: []}
heartRates = {Awake: [], Light/Core: [], Deep: [], REM: []}

#output of avgSleep, this should be initialized in main
totalAverages = {Awake: [], Light/Core: [], Deep: [], REM: []}

def avgSleep(sleepHours):
    for key in sleepHours:
        total = 0
        for value in sleepHours[key]:
            total+= value
        avg = total/len(sleepHours[key])
        totalAverages[key].append(avg)
        
def avgHR(heartRates):
    for key in heartRates:
        total = 0
        for value in heartRates[key]:
            total+= value
        avg = total/len(heartRates[key])
        totalAverages[key].append(avg)
<<<<<<< HEAD
        
        
    
=======
>>>>>>> 4e753fbfe507d3dc14e6ce8541231be1ccbd90ae
