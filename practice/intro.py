from datetime import datetime

def calculateBirthAge(year):
    if( year):

        print(datetime.now().year - year)
        print(datetime.now().date())

calculateBirthAge(1996)