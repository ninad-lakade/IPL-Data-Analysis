import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_matches_btdata.csv')
df = pd.DataFrame(data, columns = ['ball_num', 'batter_id', 'non-striker_id', 'bowler_id', 'speed', 'player_dismissed', 'dismissal_desc' ,'total_runs', 'runs', 'bowler_extras', 'extra_type', 'otw', 'length', 'line', 'line_at_stumps', 'height_at_stumps', 'shot_dist0', 'shot_dist1','match_id', 'match_inn', 'over_ball', 'over_num', 'deviation', 'batter_name', 'bowler_name', 'bat_style', 'bowl_style', 'batting_team', 'bowling_team', 'length_type', 'venue', 'year','bowler_style'])
df = df[(df['year']>=2018) & (df['year']<=2022)]
#print(df)
result = pd.DataFrame(columns = ['Batsman', 'Runs', 'Balls Faced', 'Average', 'SR', 'BP4' , 'BP6', 'DBP', 'RPO'])
for i in df['batter_name'].unique():
    #print(i)
    df1 = (df[(df['batter_name']== i) ])
    #print(df1)
    wicket_type = []
    new = df1['dismissal_desc'].tolist()
    for j in new:
        j = str(j)
        if j[0]=='c':
             wicket_type.append("caught")
        elif j[0]=='b':
             wicket_type.append("bowled")
        elif j[0]=='l':
             wicket_type.append("lbw")
        elif j[0]=='s':
             wicket_type.append("stumped")
        elif j[0]=='r':
             wicket_type.append("run out")
        elif j[0]=='h':
             wicket_type.append("hit wicket")
        else: 
             wicket_type.append(None)   
    #print(len(wicket_type))
    #print(len(df))
    df1['wicket_type'] = wicket_type
    df2 = (df1[(df1['over_num'] > 1) & (df1['over_num'] < 21) & (df1['match_inn'] < 3)])
    #print(len(df1))
    df3 = df2[(((df2['wicket_type']=='caught') | (df2['wicket_type'] == 'bowled') | (df2['wicket_type'] == 'run out') | (df2['wicket_type']=='lbw') | (df2['wicket_type'] == 'caught and bowled') | (df2['wicket_type'] == 'stumped') | (df2['wicket_type'] == 'hit wicket')))]
    #print(len(df2))
    index = df3.index
    wickets = len(index)
    df4 = df2
    index = df4.index
    balls = len(index)
    wides = 0
    noballs = 0
    new1 = df4['extra_type'].tolist()
    for k in new1:
        k= str(k)
        if k[0]=='W':
            wides = wides + 1
        elif k[0]=='N':
            noballs = noballs + 1
    
    runs = df4['runs'].sum()
    balls = balls - wides
    if wickets > 0:
        strike_rate = (runs/balls)*100
    else:
        strike_rate = 0
    if wickets > 0:
        average = runs/wickets
    else:
        average = 0
    df5 = df4[df4['runs'] == 4]
    index = df5.index
    count_four = len(index)
    df6 = df4[df4["runs"] == 6]
    index = df6.index
    count_six = len(index)
    df7 = df4[df4["runs"] == 0]
    index = df7.index
    count_dot= len(index) - wides
    #print(i)
    #print(runs)
    #print(balls)
    #print(strike_rate)
    if count_four > 0:
        BP4 = balls/count_four
    else:
        BP4 = 0
    if count_six > 0:
        BP6 = balls/count_six
    else:
        BP6 = 0
    if balls > 0:
        DBP = (count_dot/balls)*100
    else:
        DBP = 0
    if balls > 0:
        DBP = (count_dot/balls)*100
    else:
        DBP = 0
    if balls > 0:
        RPO = (runs/balls)*6
    else:
        RPO = 0
    
    #print(average)
    #print(count_four)
    #print(count_six)
    #print(count_dot)
    if ((balls > 60)) :
        df8 = pd.DataFrame({"Batsman":[i], "Runs":[runs], "Balls Faced": [balls], "Average":[average], "SR":[strike_rate], "BP4":[BP4], "BP6": [BP6], "DBP": [DBP], "RPO": [RPO]})
        result = result.append(df8)
        #print(result)
result.sort_values(by=['SR'], inplace=True, ascending=False)
#result.sort_values(by=['SR'], inplace=True, ascending=False)
final = result.round(decimals=2)
print(final)
plt.scatter(final.Batsman, final.SR)
plt.scatter(final.Batsman, final.Average)
plt.figure(figsize = (15,100))
final.to_excel(r'C:\Users\ninad\Desktop\Cricket Data\Sample DataBTLIST.xlsx', index = False)
