from datetime import date
import math

#ask user start date (and eventually a Y/N prompt if they would like to use the current day)
yearStart = int(input("Start Year: "))
monthStart = int(input("Start Month (numerical): "))
dayStart = int(input("Start Day: "))
print("--------------")
yearEnd = int(input("End Year: "))
monthEnd = int(input("End Month (numerical): "))
dayEnd = int(input("End Day: "))

class ChosenDay:
  def __init__(self, yearStart, monthStart, dayStart, yearEnd, monthEnd, dayEnd):
      self.yearStart = yearStart
      self.monthStart = monthStart
      self.dayStart = dayStart
      self.yearEnd = yearEnd
      self.monthEnd = monthEnd
      self.dayEnd = dayEnd
      print("-----------------------")
  #substraction of the days
  def calculateDays(self):
    selected_day = date(self.yearEnd, self.monthEnd, self.dayEnd)
    start_day = date(self.yearStart, self.monthStart, self.dayStart)
    days_for_selected_day = (selected_day - start_day)
    return  days_for_selected_day
  #print days
  def printDays(self):
    d = self.calculateDays()
    print(d)
    # if d < 0:
    #     d = int(math.fabs(d))
    #     print(str(d) + " DAYS AGO!")
    # elif d > 0:
    #     print(str(d) + " DAYS LEFT!")
    # else:
    #     print("TODAY!")
#check if month is over 12
if monthEnd <= 0 or monthEnd > 12:
    print("Invalid Month")
else:
    xmasDays = ChosenDay(yearStart, monthStart, dayStart, yearEnd, monthEnd, dayEnd)
    xmasDays.printDays()