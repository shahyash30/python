import time

timestamp = int(time.strftime('%H'))
print(timestamp)

if(timestamp>0 and timestamp<12):
    print('good mrng')
elif(timestamp==12):
    print('happy noon')
elif(timestamp>12 and timestamp<17):
    print('good evng')
else:
    print('GOod nyt')