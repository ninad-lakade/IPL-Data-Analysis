import pandas as pd
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\ipl_matches_btdata.csv')
df = pd.DataFrame(data, columns = ['ball_num', 'batter_id', 'non-striker_id', 'bowler_id', 'speed', 'player_dismissed', 'dismissal_desc' ,'total_runs', 'runs', 'bowler_extras', 'extra_type', 'otw', 'length', 'line', 'line_at_stumps', 'height_at_stumps', 'shot_dist0', 'shot_dist1','match_id', 'match_inn', 'over_ball', 'over_num', 'deviation', 'batter_name', 'bowler_name', 'bat_style', 'bowl_style', 'batting_team', 'bowling_team', 'length_type', 'venue', 'year','bowler_style'])
df = df[(df['year']>=2018) & (df['year']<=2022)]
#print(len(df))
name = ("Rishabh Pant")
wicket_type = []
new = df['dismissal_desc'].tolist()
for i in new:
    i= str(i)
    if i[0]=='c':
         wicket_type.append("caught")
    elif i[0]=='b':
         wicket_type.append("bowled")
    elif i[0]=='l':
         wicket_type.append("lbw")
    elif i[0]=='s':
         wicket_type.append("stumped")
    elif i[0]=='r':
         wicket_type.append("run out")
    elif i[0]=='h':
         wicket_type.append("hit wicket")
    else: 
         wicket_type.append(None)
print(len(wicket_type))
print(len(df))
df['wicket_type'] = wicket_type

df1 = (df[(df['over_num'] > 16) & (df['over_num'] < 21) & (df['match_inn'] < 3)])
print(len(df1))
df2 = df1[(((df1['wicket_type']=='caught') | (df1['wicket_type'] == 'bowled') | (df1['wicket_type'] == 'run out') | (df1['wicket_type']=='lbw') | (df1['wicket_type'] == 'caught and bowled') | (df1['wicket_type'] == 'stumped') | (df1['wicket_type'] == 'hit wicket')))]
print(len(df2))
index = df2.index
wickets = len(index)
df3 = df1
index = df3.index
balls = len(index)
wides = 0
noballs = 0
new1 = df3['extra_type'].tolist()
for i in new1:
    i= str(i)
    if i[0]=='W':
        wides = wides + 1
    elif i[0]=='N':
        noballs = noballs + 1

runs = df3['runs'].sum()
balls = balls - wides
strike_rate = (runs/balls)*100
average = runs/wickets
df4 = df3[df3['runs'] == 4]
index = df4.index
count_four = len(index)
df5 = df3[df3["runs"] == 6]
index = df5.index
count_six = len(index)
df6 = df3[df3["runs"] == 0]
index = df6.index
count_dot= len(index) - wides
print("Batsman:", name)
print("Runs Scored: ", runs)
print("Balls Faced: ", balls)
print("Average: ", round(average,2))
print("Strike-rate: ", round(strike_rate,2))
print("BPF: ", round((balls/count_four),2))
print("BPS: ", round((balls/count_six),2))
print("DBP: ", round((count_dot/balls)*100,2))
#plt.scatter(name, strike_rate)

