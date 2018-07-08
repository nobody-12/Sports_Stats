from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
forever=1

with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
    for line in response:
        line=line.decode('utf-8')
        if '0' in line:
            x=line
            print(x[-2:])


