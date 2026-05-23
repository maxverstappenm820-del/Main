#python countdown timer program

import time
my_time = int(input("Enter the time in seconds: "))

#we can use while loop instead of for loop
#we can use reverse() function insted of -1 in for loop
for x in range(my_time, 0, -1):
    seconds=int(x % 60)
    minutes=int((x // 60) % 60)
    hours=int((x // 3600))
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("Time's up!")


  
    