from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
total_counter=-1
average=0
find_avg=0
with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
    for line in response:
        line=line.decode('utf-8')
        if '0' or '1' in line:
            x=line
            y=x[-2:]
            total_counter=total_counter+1
            if '0' in y:
                pass
            elif '1' in y:
                find_avg=find_avg+1
             
                
print('The percentage of wins by a home team in the 2017,18 season is',round(find_avg/total_counter,2), end = '%\n')
