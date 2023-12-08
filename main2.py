import time 

starttime = time.time()

while True :
    from time import strftime
    string = strftime('%H:%M:%S')
    print(string)
    time.sleep(1.0 - ((time.time() - starttime) % 1.0))