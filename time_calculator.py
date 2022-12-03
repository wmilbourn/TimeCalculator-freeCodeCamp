def add_time(start, duration, weekday=None):
  x = start.partition(" ") #breaks time string into three parts
  startHour = x[0].split(":")[0] #extracts the hour from the start timestamp
  startMin = x[0].split(":")[1] #extracts the minutes from the start timestamp
  AmPm = x[2] #indicates AM or PM
  newAmPm = ""
  days = 0
  weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
  global new_time 
  y = duration.partition(":") #breaks duration string into three parts
  addHour = y[0] #extracts hours from duration
  addMin = y[2] #extracts minutes from duration

    #converting 24 hrs or more into days to define remaining hours to add
  if int(addHour) > 23:
    convertDay = divmod(int(addHour), 24)
    days = days + convertDay[0]
    addHour = convertDay[1]
  else: #is this part necessary?
    addHour = addHour

  sumHour = int(startHour) + int(addHour)
  sumMin = int(startMin) + int(addMin)

    #converting minutes over 60 to hours and minutes
  if sumMin > 59: 
    hrMin = divmod(sumMin, 60)
    hr = hrMin[0]
    minutes = hrMin[1]
    sumMin = minutes
    if sumMin < 10: #adding a 0 at the beginning in if the minutes are less than 10
        sumMin = "0"+str(sumMin)
    sumHour = sumHour + hr
  
  if len(str(sumMin)) < 2: #adding a 0 at the beginning in if the minutes are less than 10
      sumMin = "0"+str(sumMin)

    #making it 12-hour display
  if sumHour >= 12: 
    if AmPm == "AM": #changing AM to PM if it goes past 11AM
        newAmPm = "PM"
    elif AmPm == "PM": #changing PM to AM if it goes past 11PM
      newAmPm = "AM"
      days += 1 #adds 1 day
    if sumHour > 12: #converting to the 12 hour display
        absHour = abs(12-sumHour)  
        new_time = str(absHour) + ":" + str(sumMin) + " " + newAmPm
    else: 
        new_time = str(sumHour) + ":" + str(sumMin) + " " + newAmPm
  else: #if no conversions were needed
    new_time = str(sumHour) + ":" + str(sumMin) + " " + str(AmPm)

  #if the optional weekday argument was included
  if weekday != None: 
    formatWeekday = str(weekday.lower().capitalize()) #properly format the weekday
    d = weekdays.index(formatWeekday) #index the day from previously defined weekday variable
    if days == 0:
      return new_time + ", " + str(formatWeekday)
    else:
      weekdayNum = d + days
      if weekdayNum > 6: #circling back since there are only 7 days in a week
        newWeekday = divmod(weekdayNum, 7)
        newDays = newWeekday[1]
        endDay = weekdays[newDays]
        if days == 1:
          return new_time + ", " + str(endDay) + " (next day)"
        else:   
          return new_time + ", " + str(endDay) + " (" + str(days) + " days later)"
      else:
        endDay = weekdays[weekdayNum]
    if days == 1:
      return new_time + ", " + str(endDay) + " (next day)"
    else:
      return new_time + ", " + str(endDay) + " (" + str(days) + " days later)"
  else: #if the optional weekday argument was not included
    if days == 0:
      return new_time
    elif days > 1:
      return new_time + " (" + str(days) + " days later)"
    elif days == 1:
      return new_time + " (next day)"

  

#print(add_time("2:59 AM", "24:00", "saturDay"))


  