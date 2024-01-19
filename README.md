
# Sleepify Wrapped
## About
Inspired by the annually released Spotify Wrapped, we aimed to create a program that summarizes sleep schedules and quality. We centered our programming decisions around the data available to us. Using 9 months of a [Kaggle user's Apple Health data](https://www.kaggle.com/datasets/aeryss/apple-health-sleep-stages-and-heart-rate?resource=download), we identified four primary sleep categories (as tracked by Apple Watch devices): Awake, Light/Core, Deep, and REM. 

| Category | Description* |
| ----------- | ----------- |
| Awake | Title |
| Light/Core | Text |
| Deep | Title |
| REM | Text |
*According to Apple

Sleepify Wrapped informs the user on the average number of hours slept in each category as well as the average heart rate (BPM) for each category. Why is this useful? We know adults should get at least 7 hours of sleep every night, but many people who reach this goal continue to feel unrested. That's where our program proves useful: it combines lesser-known knowledge of sleep cycles with the user's personal data, helping them pinpoint the underlying problem. For example, people whose REM sleep is continuously disrupted may find it more difficult

## Ethical Considerations
As college students with no medical background, we want to make it abundantly clear that this program should not be used to diagnose sleep disorders. In addition to summarizing datta in a concise and useful manner, it is purely meant to democratize knowledge on sleep quality and how it affects all of us in our daily lives.

## Future Directions
As a group, we had 12 hours to code this project. With the time constraint, we 



The data provides a 'Start Time' and 'End Time' column for tracking the duration of each sleep type. These times are provided in a 'MONTH/DAY/YR HR:MIN:SEC AM/PM' format. In order to accumulate times in terms of of their sleep type and day, we needed to extract the desired definition of time accordingly. We developed the following methods:

### calculateSleepDuration()
This method calculates the TOTAL duration of sleep per night. Using the calculateSleepDifference() function within the main function, we iterate through each row and recieve total sleep duration per sleep type. The total time is returned as a double rounded to the tenths.

### calculateSleepDifference()
This is a helper method, specifically used to assist in time conversions for the calculateSleepDuration() function. The night is organized into different time blocks according to the different types of sleep experienced by the user. The time stamp is extracted from the 'End Time' and 'Start Time' columns, then each is converted into a their equivalent in minutes (E.g. hours converted to 60 minutes whilst minutes amount remains the same). The "total start time" is then subtracted from the "total end time", resulting in the total time passing within that block. The total time is returned as a double rounded to the tenths.

### minToHrs(min)
This is a helper method that inputs an int representing minutes and converts the provided minutes to hours. This method is used within the calculateSleepDifference() method. The total time is returned as a double rounded to the tenths.

### hrsToMin(hrs)
This is a helper method that inputs an int representing time in hours and converts the provided hours to minutes. This method is used within the calculateSleepDifference() method. The total time is returned as a double rounded to the tenths.

### minToSec(min)
This is a helper method that inputs an int representing time in minutes and converts the provided minutes to seconds. This method is used within the calculateSleepDifference() method. The total time is returned as a double rounded to the tenths.

### timeRetrieve(cell)
This is a helper method that that inputs a cell's contents and retrieves the time stamp from the 'Start Time' or 'End Time' column from their provided 'MONTH/DAY/YR HR:MIN:SEC AM/PM' format. The date is returned as a string.

### dateRetrieve(cell)
This is a helper method that inputs a cell's contents and retrieves the date stamp from the 'Start Time' or 'End Time' column from their provided 'MONTH/DAY/YR HR:MIN:SEC AM/PM' format. The date is returned as a string.

### avgSleep(sleepHrs, listOfAverages)
This is a method that uses the data gathered to calculate the average number hours of sleep per sleep type. The total is returned as a double rounded to the tenths. 

### avgHR(heartRates, listOfAverages)
This is a method that uses the data gatheered to calculate the average heartrate experienced per sleep type. The total is returned as an int. 

### getHR(row, listOfHeartRates)
This is a getter method and assists the avgHR() function. The resulting output is an int representing the heartrate. 

### main(filename)
This function inputs a file name, opens the provided file, and runs all methods accordingly. Sleep hours and heart rates are organized in coordination to their associated sleep type, using a dict data structure for easy accessibility by keys (sleep types). The program begins by looping through the dataset, beginning this organization of data. We then calculate the averages using the information gathered within these structures. If time had permit, we would have enjoyed being able to present these averages as well as other details regarding dreams, health risks, and health tips. 
