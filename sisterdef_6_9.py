
minute = int(raw_input('Please input one minute num: '))

if (minute < 60):
    print minute, ' minute'
else:
    hour = minute / 60;
    minute = minute % 60
    print hour, ' hour', minute, 'minute'