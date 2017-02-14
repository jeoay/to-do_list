from datetime import datetime
from datetime import time
from datetime import timedelta

### gets current time and date
now = datetime.now()

### defines how much time is left in the day to do these tasks
def time_left():
   # pulls in current time 
    current_time = now.time()
   # creates a variable with the time the sun goes down
    dusk = current_time.replace(hour=17,minute=0,second=0,microsecond=0)
   # pulls the hour out of the time
    current_hour = current_time.hour
    dusk_hour = dusk.hour
   # converts time into a string and prints current time
    current_time = now.strftime("%X")
    dusk = dusk.strftime("%X")
    print "The current time is " + current_time + " pst."
   # makes sunlight global and creates integer for how much sunlight is left in the day
    global sunlight
    sunlight = dusk_hour - current_hour
   # removes the "s" in "hours" if sunlight == 1 
    if sunlight == 1:
        print "The sun will go down in " + str(sunlight) + " hour."
    else:
        print "The sun will go down in " + str(sunlight) + " hours."
        

time_left()
print "_____________________________________________________"
        
### to-do list array and print with #'s and without brackets
to_do = []

# array.append('item') to add list items
to_do.append('walk dogs')
to_do.append('Work on Web Dev')
to_do.append('Install printer ink')
# del array[#] to delete


for num, stuff in enumerate(to_do):
    print str(num) + ": " + stuff.upper()
