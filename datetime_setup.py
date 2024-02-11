# DateTime modules

from datetime import datetime

current_time = datetime.now()

print(type(current_time))
print(current_time)

# formating datetime object as a string using isoformat
current_time = current_time.isoformat()
 # or
# current_time = current_time.strftime('%Y-%m-%dT%H:%M:%S.%f')
 # or
# current_time = current_time.strftime('%Y-%m-%d  %H:%M:%S.%f')

print(type(current_time))
print(current_time)

# coverting the datetime string back to datetime object
current_time = datetime.fromisoformat(current_time)
 # or
# current_time = datetime.strtime(current_time, '%Y-%m-%d  %H:%M:%S.%f')

print(type(current_time))
print(current_time)