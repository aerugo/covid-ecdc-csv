# Alarm indicator on country-level

## SUMMARY
This script feeds the latest ECDC data on the Covid-19 outbreak to a spreadsheet and calculates if a country looks like it may be heading for a high number casualties. It also shows deaths as a percentage of country population, to measure severity for society. 

See the spreadsheet here. All calculations are done in the spreadsheet, the script only provides raw data. Only current processing is to remove the cruise ship rows from the dataset and only keep countries.

## DISCLAIMER:
This is my own work. I am not a professional in this field. My highest qualification is a degree in biotechnology and bioinformatics, which is barely related to this at all, apart from making me comfortable with looking at data. I made this to satisfy my own curiosity and thought others might benefit.

## WHY
What I worry most about are the cases overwhelming the health care systems. This happens at very different times in different countries. Some countries are able to mitigate better than others. Some countries have more resilient health care systems. Others do social distancing better or are just less densely populated.
I have friends all over the world, and I worry about them. It's too hard to understand what might be about to happen on a country level when just looking at the number of new cases or deaths.

## HOW DOES IT WORK?
A spreadsheet gets the ECDC data and runs some calculations that I have defined myself. A script pulls the ECDC data from an official Excel and puts it on GitHub as a CSV. I need to remember to run and update it every day, but that is only three commands and takes 30 seconds. Its main purpose is to list all countries along with an "ALARM" column which is meant to indicate if a certain country might starting to strain its health care systems like what happened in Northern Italy. 

One important metric in this calculation is the C7 number, the number of cases confirmed 7 days ago. This is based on the assumption that it takes people on average one week to die, if they die. This number is not meant to be exact, but just a very rough approximation.

Another important metic is the dDa number. It is the difference between new deaths and new days the day before, looked at for 2 days for the current date or 3 days for historical data, and divided by 2 or 3 accordingly.

This is how I calculate if a country gets an alarm:

**C** = Confirmed cases

**C7** = Confirmed cases 7 days ago

**dDa** = Growth of new deaths, averaged over 2 days (for todays data) or 3 days (older data)

**Ai** (Alarm index) =  **dDa** * (**C**/**C7**)

**Ait** = Alarm index today

**Aiy** = Alarm index yesterday 

**As** (Alarm signal) = "ALARM" if **Ait** > **Aiy** and **Ait** > 1

Finally, I show a country as having an alarm for a given day if it evaluates as an alarm for any day around it +-3. When only considering todays data, this means in that a country is rated as having an alarm if it has had an alarm within the last 4 days.

I also calculate the casualty rate as a proportion of country population. 
