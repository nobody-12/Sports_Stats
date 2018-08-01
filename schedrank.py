print(''' This is my explanation, 
it should cover how to use this algorithm
''')

from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#input sources for scraping

omni = input('What sector would you like to know: ') #raw imput
''' 
Source code for the all teams function, this function takes the win percentages of all the teams
'''
def allTeams():
    factcheck = []
    team1=[]
    ran=0
    nn=0
    length = []
    playoffs = []
    infin = 0
    total = 31
    with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
        for line in response:
            line=line.decode('utf-8')
            string = line
            strings = line[20:23]
            team2 = strings.replace(',','')
            team1.append(team2)
        team = team1[1:]
        original = list(set(team))
    while ran<31:
        ran=ran+1
        nn=0
        with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
            for line in response:
                line=line.decode('utf-8')
                aa = line[20:27]
                bb = aa.replace('1','')
                if original[ran] in bb:
                    nn=nn+1

        playoffs.append(original[ran])
    print(playoffs)
    while infin < total:
        sh = -1
        t = playoffs[infin]
        infin=infin+1
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
            ga1 = num.replace(',','')
            ga2 = ga1.replace(ga1[-1],'')
            ga = int(ga2.replace(' ',''))
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
                    ag=ag-1
                    thing = quien[ag-1]
                    if opp in thing[:3] and '1' in thing[-1]:
                        win=win+1
                    elif opp not in thing [:3] and '0' in thing[-1]:
                        win=win+1
            #print('after the',te,'vs',opp, 'game finished,',opp, 'had', win,'wins out of',ga,'games, giving it a win percentage of',str(int(round(win/ga,2)*100))+'%')
            numvalue.append(int(round(win/ga,2)*100))
            value = round(round(sum(numvalue)/(length+1),2)-50,2)
        if round(sum(numvalue)/(length+1),2) > 50:
            higher = 'higher'
        else: 
            higher = 'lower'
            value=value*-1
        print('The average win percent of the opponents of',te,'was',str(round(sum(numvalue)/(length+1),2))+'%','which is',higher,'than average by',str(value)+'%')
        factcheck.append(value)
    print('The value for a error is approximately +0.14 (error happens because of rounding) out of 16.0 or an average error value of approximately +0.004 (0.04%) per team and an approximate error value of 0.0005 (0.005%)')
"""





"""
def badTeams():
    team1=[]
    ran=0
    nn=0
    length = []
    playoffs = []
    infin = 0
    with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
        for line in response:
            line=line.decode('utf-8')
            string = line
            strings = line[20:23]
            team2 = strings.replace(',','')
            team1.append(team2)
        team = team1[1:]
        original = list(set(team))
    while ran<31:
        ran=ran+1
        nn=0
        with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
            for line in response:
                line=line.decode('utf-8')
                aa = line[20:27]
                bb = aa.replace('1','')
                if original[ran] in bb:
                    nn=nn+1
        if nn==16:
            playoffs.append(original[ran])
    print(playoffs)
    while infin < 19:
        sh = -1
        t = playoffs[infin]
        infin=infin+1
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
            ga1 = num.replace(',','')
            ga2 = ga1.replace(ga1[-1],'')
            ga = int(ga2.replace(' ',''))
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
                    ag=ag-1
                    thing = quien[ag-1]
                    if opp in thing[:3] and '1' in thing[-1]:
                        win=win+1
                    elif opp not in thing [:3] and '0' in thing[-1]:
                        win=win+1
            #print('after the',te,'vs',opp, 'game finished,',opp, 'had', win,'wins out of',ga,'games, giving it a win percentage of',str(int(round(win/ga,2)*100))+'%')
            numvalue.append(int(round(win/ga,2)*100))
            value = round(round(sum(numvalue)/(length+1),2)-50,2)
        if round(sum(numvalue)/(length+1),2) > 50:
            higher = 'higher'
        else: 
            higher = 'lower'
            value=value*-1
        print('The average win percent of the opponents of',te,'was',str(round(sum(numvalue)/(length+1),2))+'%','which is',higher,'than average by',str(value)+'%')

def greaTeams():
    team1=[]
    ran=0
    nn=0
    length = []
    playoffs = []
    infin = 0
    with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
        for line in response:
            line=line.decode('utf-8')
            string = line
            strings = line[20:23]
            team2 = strings.replace(',','')
            team1.append(team2)
        team = team1[1:]
        original = list(set(team))
    while ran<31:
        ran=ran+1
        nn=0
        with urlopen('https://projects.fivethirtyeight.com/nfl-api/2017/nfl_games_2017.csv') as response:
            for line in response:
                line=line.decode('utf-8')
                aa = line[20:27]
                bb = aa.replace('1','')
                if original[ran] in bb:
                    nn=nn+1
        if nn>16:
            playoffs.append(original[ran])
    print(playoffs)
    while infin < 11:
        sh = -1
        t = playoffs[infin]
        infin=infin+1
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
            ga1 = num.replace(',','')
            ga2 = ga1.replace(ga1[-1],'')
            ga = int(ga2.replace(' ',''))
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
                    ag=ag-1
                    thing = quien[ag-1]
                    if opp in thing[:3] and '1' in thing[-1]:
                        win=win+1
                    elif opp not in thing [:3] and '0' in thing[-1]:
                        win=win+1
            #print('after the',te,'vs',opp, 'game finished,',opp, 'had', win,'wins out of',ga,'games, giving it a win percentage of',str(int(round(win/ga,2)*100))+'%')
            numvalue.append(int(round(win/ga,2)*100))
            value = round(round(sum(numvalue)/(length+1),2)-50,2)
        if round(sum(numvalue)/(length+1),2) > 50:
            higher = 'higher'
        else: 
            higher = 'lower'
            value=value*-1
        print('The average win percent of the opponents of',te,'was',str(round(sum(numvalue)/(length+1),2))+'%','which is',higher,'than average by',str(value)+'%')


def selecTeam():
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
        ga1 = num.replace(',','')
        ga2 = ga1.replace(ga1[-1],'')
        ga = int(ga2.replace(' ',''))
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
                ag=ag-1
                thing = quien[ag-1]
                if opp in thing[:3] and '1' in thing[-1]:
                    win=win+1
                elif opp not in thing [:3] and '0' in thing[-1]:
                    win=win+1
        print('after the',te,'vs',opp, 'game finished,',opp, 'had', win,'wins out of',ga,'games, giving it a win percentage of',str(int(round(win/ga,2)*100))+'%')
        numvalue.append(int(round(win/ga,2)*100))
        value = round(round(sum(numvalue)/(length+1),2)-50,2)
    if round(sum(numvalue)/(length+1),2) > 50:
        higher = 'higher'
    else: 
        higher = 'lower'
        value=value*-1
    print('The average win percent of the opponents of',te,'was',str(round(sum(numvalue)/(length+1),2))+'%','which is',higher,'than average by',str(value)+'%')

if omni == "s":
    selecTeam()
elif omni == 'p':
    greaTeams()
elif omni == 'n' or omni=='b':
    badTeams()
elif omni == 'a':
    allTeams()
else: 
    print('invalid input\nprocess terminated')
