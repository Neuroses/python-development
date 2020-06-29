import yagmail
import time
import datetime

EmailAddress = input("Type the email you want to send the reminder from (it can be the same one you want it sent to) and press enter: ")
EmailPassword = input("Type the password to the email you just gave and press enter: ")
ReminderReciever = input("Type the email you want the reminder to be sent to and press enter: ")
ReminderFile = input("Type the name of the file with your reminder in it and press enter: ")
ReminderMonth = input("Type the number of the month (1, 2, 10, 11, etc) you want to be reminded and press enter: ")
ReminderDay = input("Type the day of the month (7, 15, 28, etc) you want to be reminded and press enter: ")
ReminderHour = input("Type the hour (in 24 hour format) you want to be reminded and press enter: ")
ReminderMinute = input("Type the minute you want to be reminded and press enter: ")

print("Ok, you'll be reminded:")

if ReminderMonth == "1":
    print("January")
elif ReminderMonth == "2":
    print("February")
elif ReminderMonth == "3":
    print("March")
elif ReminderMonth == "4":
    print("April")
elif ReminderMonth == "5":
    print("May")
elif ReminderMonth == "6":
    print("June")
elif ReminderMonth == "7":
    print("July")
elif ReminderMonth == "8":
    print("August")
elif ReminderMonth == "9":
    print("September")
elif ReminderMonth == "10":
    print("October")
elif ReminderMonth == "11":
    print("November")
elif ReminderMonth == "12":
    print("December")
else:
    print("you clearly didnt say a month 1-12 so youre either stupid or bad at typing")

if ReminderDay == "1":
    print("1st")
elif ReminderDay == "2":
    print("2nd")
elif ReminderDay == "3":
    print("3rd")
elif ReminderDay == "4":
    print("4th")
elif ReminderDay == "5":
    print("5th")
elif ReminderDay == "6":
    print("6th")
elif ReminderDay == "7":
    print("7th")
elif ReminderDay == "8":
    print("8th")
elif ReminderDay == "9":
    print("9th")
elif ReminderDay == "10":
    print("10th")
elif ReminderDay == "11":
    print("11th")
elif ReminderDay == "12":
    print("12th")
elif ReminderDay == "13":
    print("13th")
elif ReminderDay == "14":
    print("14th")
elif ReminderDay == "15":
    print("15th")
elif ReminderDay == "16":
    print("16th")
elif ReminderDay == "17":
    print("17th")
elif ReminderDay == "18":
    print("18th")
elif ReminderDay == "19":
    print("19th")
elif ReminderDay == "20":
    print("20th")
elif ReminderDay == "21":
    print("21st")
elif ReminderDay == "22":
    print("22nd")
elif ReminderDay == "23":
    print("23rd")
elif ReminderDay == "24":
    print("24th")
elif ReminderDay == "25":
    print("25th")
elif ReminderDay == "26":
    print("26th")
elif ReminderDay == "27":
    print("27th")
elif ReminderDay == "28":
    print("28th")
elif ReminderDay == "29":
    print("29th")
elif ReminderDay == "30":
    print("30th")
elif ReminderDay == "31":
    print("31st")
else:
    print("how the fuck you want me to tell you when it's a day of the month that doesnt happen")

if ReminderHour <= "12":
    print('At', ReminderHour,':',ReminderMinute,'AM')
elif ReminderHour >= "12":
    print('At', ReminderHour,':',ReminderMinute,'PM')


t = datetime.datetime.today()
future = datetime.datetime(t.year,int(ReminderMonth),int(ReminderDay),int(ReminderHour),int(ReminderMinute))
if t.hour >= 2:
    future += datetime.timedelta(days=1)
time.sleep((future-t).seconds)

yag = yagmail.SMTP(EmailAddress, EmailPassword)
subject = "Reminder"
contents = [
   "Reminder", ReminderFile
]
yag.send(ReminderReciever, subject, contents)

print("Reminder Sent")