from datetime import datetime
from datetime import time
from datetime import timedelta

### gets current time and date
now = datetime.now()

### Am I done with work?
work = "done"

### to-do list array and print without brackets
to_do = ["rake backyard", "construct organizer", "walk the dogs", "work", "go to dinner", "go to gym"]
print "Need to do: " + ', '.join(to_do) + "."

#### defines how much time is left in the day to do these tasks
# def time_left():
#    ### pulls in current time 
#     current_time = now.time()
#    ### creates a variable with the time the sun goes down
#     dusk = current_time.replace(hour=17,minute=0,second=0,microsecond=0)
#    ### pulls the hour out of the time
#     current_hour = current_time.hour
#     dusk_hour = dusk.hour
#    ### converts time into a string and prints current time
#     current_time = now.strftime("%X")
#     dusk = dusk.strftime("%X")
#     print "The current time is " + current_time + " pst."
#    ### makes sunlight global and creates integer for how much sunlight is left in the day
#     global sunlight
#     sunlight = dusk_hour - current_hour
#    ### removes the "s" in "hours" if sunlight == 1 
#     if sunlight == 1:
#         print "The sun will go down in " + str(sunlight) + " hour."
#     else:
#         print "The sun will go down in " + str(sunlight) + " hours."
# 
# def rake_backyard():
#     print "Backyard is clean of leaves"
# 
# def construct_organizer():
#     print "Organizer in office has been constructed"
#     
# def do_work():
#     print "Get back to work"
#     
# def complete_task():
#     time_left()
#     if work == "done" and sunlight >= 1:
#         rake_backyard()
#     elif work == "done" and sunlight <1:
#         construct_organizer()
#     else:
#         do_work()
# 
# 
# complete_task()
