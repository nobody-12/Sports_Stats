from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
total_counter=-1
forever=267
find_avg=0
score_1 = 0
change = 2
with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
    for line in response:
        line=line.decode('utf-8')
        if '0' in line:
            x=line
            y=x[-8:-3]
            #print(y)
            if ',' in y[0]:
                pass
            else: 
                print(y[0:2])
                print(y[3:5])
               
