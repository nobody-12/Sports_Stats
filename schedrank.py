from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
sh = -1
t = input("What team: ")
te = t.upper()
ii = 0
numvalue = []
with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
    for line in response:
        line=line.decode('utf-8')
        aa = line[20:27]
        bb = aa.replace('1','')
        if te in bb:
            ii=ii+1
    length = int(ii)-1
while sh<length:
    ga = int(0)
    sh = sh+1
    ga=ga+1
    record = []
    i=0
    n=0
    orecord = []
    win = 0


    with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
        for line in response:
            line=line.decode('utf-8')
            x=line[20:27]
            y = x.replace('1','')
            if te in y:
                yy = y.replace(',',' ')
                oth = yy.replace(te,'')
                i=i+1
                record.append(oth+' '+str(i)+' '+y[-1]) 
    var = record[sh]
    if ' ' in var[0]:
        opp1 = var[0:4]
    else:
        opp1 = var[:3]
    opp = opp1.replace(' ','')
    num = var.replace(opp,'')
    ga = int(num.replace(',',''))
    ag = ga




    with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
            for line in response:
                line=line.decode('utf-8')
                a = line[20:27]
                b = a.replace('1', '')
                x=line[20:27]
                y = x.replace('1','')
                if opp in b:
                    orecord.append(y+' '+line[-2])
                    new = y[:3]
                quien = orecord[:ga]
    while ag > 0 :
            thing = quien[ag-1]
            ag=ag-1
            if opp in thing[:3] and '1' in thing[-1]:
                win=win+1
            elif opp not in thing [:3] and '0' in thing[-1]:
               win=win+1
    print('after the game finished',opp, 'had', win,'wins out of',ga,'games, giving it a win percentage of',str(int(round(win/ga,2)*100))+'%')
    numvalue.append(int(round(win/ga,2)*100))
if round(sum(numvalue)/(length+1),2) > 50:
    higher = 'higher'
else: 
    higher = 'lower'
print('The average win percent of the opponents of',te,'was',str(round(sum(numvalue)/(length+1),2))+'%','which is',higher,'than average by',str(round(round(sum(numvalue)/(length+1),2)-50,2))+'%')
