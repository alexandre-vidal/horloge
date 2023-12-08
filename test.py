import datetime
import time

def afficher_heure(): 
    starttime = time.time()
    while True :
        from time import strftime
        if alarm == "oui":
            if alarm_heure == strftime('%H:%M:%S'):
                print("Dring Dring")
        string = strftime('%H:%M:%S')
        print(string)
        time.sleep(1.0 - ((time.time() - starttime) % 1.0))
    
        
def alarme(alarm_heure):
    invalid = True

    while invalid:
        userInput = alarm_heure
        
        alarmTime = [int(n) for n in userInput.split(":")]
        
        
        if alarmTime[0] >= 24 or alarmTime[0] < 0:
            print("Votre valeur est incorrecte")
            alarm_heure = input("Entrez une heure valide pour l'alarme (Ex. 06:30:00) : ")
            invalid = True
        elif alarmTime[1] > 60 or alarmTime[1] < 0:
            print("Votre valeur est incorrecte")
            alarm_heure = input("Entrez une heure valide pour l'alarme (Ex. 06:30:00) : ")
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
            
print("Voulez-vous une alarme ?")
alarm = input("oui ou non : ")
if alarm == "oui":
    alarm_heure = input("Entrez une heure valide pour l'alarme (Ex. 06:30:00) : ")
    alarme(alarm_heure)

afficher_heure()