import datetime
import time

invalid = True

while(invalid):
    print("Entrez une heure valide pour l'alarme (Ex. 06:30)")
    userInput = input(">> ")
    
    alarmTime = [int(n) for n in userInput.split(":")]
    
    if alarmTime[0] >= 24 or alarmTime[0] < 0:
        invalid = True
    elif alarmTime[1] > 60 or alarmTime[1] < 0:
        invalid = True
    else:
        invalid = False
        
seconds_hms = [3600, 60, 1]

alarmSeconds = sum([a*b for a,b in zip(seconds_hms[:len(alarmTime)], alarmTime)])

now = datetime.datetime.now()
currentTimeInSeconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

secondsUntilAlarm = alarmSeconds - currentTimeInSeconds

if secondsUntilAlarm < 0:
    secondsUntilAlarm += 86400
    
print("L'alarme est réglée")
print("L'alarme sonnera dans %s" % datetime.timedelta(seconds=secondsUntilAlarm))

time.sleep(secondsUntilAlarm)

print("On se réveille !")