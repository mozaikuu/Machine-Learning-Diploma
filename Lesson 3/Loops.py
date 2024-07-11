from threading import *
from time import sleep , time

starttime = time.time()

IsTrue = True

def Loop1():
  count = 0
  while IsTrue:
    count += 1
    print(count)
    sleep(1)

t1 = Thread(target=Loop1) 
t1.start() 

ExitLoop = input("Press Enter to exit the loop: ")
IsTrue = False

t1.join()

print("Done")

endtime = time.time()
print(endtime - starttime)