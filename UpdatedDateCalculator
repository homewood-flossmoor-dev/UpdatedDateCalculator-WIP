from datetime import date
import math

yearStart = int(input("Start Year: "))
monthStart = int(input("Start Month (numerical): "))
dayStart = int(input("Start Day: "))

class Christmas:
  def __init__(self, year, month, day):
      self.year = year
      self.month = month
      self.day = day
      print("THERE ARE: ")
  #calculate them by hardcoding xmas date
  #substraction of the days
  def calculateDays(self):
    christmas_day = date(self.yearEnd, self.monthEnd, self.dayEnd)
    days_for_xmas = (christmas_day - date.today()).days
    return  days_for_xmas
  #print days
  def printDays(self):
    d = self.calculateDays()
    if d < 0:
        d = int(math.fabs(d))
        print(str(d) + " DAYS AGO!")
    elif d > 0:
        print(str(d) + " DAYS LEFT!")
    else:
        print(str(d) + ", TODAY!")

yearEnd = int(input("End Year: "))
monthEnd = int(input("End Month (numerical): "))
dayEnd = int(input("End Day: "))

if monthEnd <= 0 or monthEnd > 12:
    print("Invalid Month")
else:
    xmasDays = Christmas(yearEnd, monthEnd, dayEnd)
    xmasDays.printDays()
    
