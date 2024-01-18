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
