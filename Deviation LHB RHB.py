import pandas as pd
import warnings
import statistics
import math
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\mensTestHawkeyeStats.csv')
result = pd.DataFrame(columns = ['Bowler', "Balls Bowled", 'batter_type', 'sdx', 'sdy', 'net_dev', 'bowler_style'])
df = data[(data['matchId']>=7000)]
for i in df['bowler'].unique():
    df1 = df[(df['bowler']==i)]
    temp = df1[['pitchX', 'pitchY', 'rightHandedBat', 'bowlingStyle']]
    newdata = temp.dropna()
    rhb = newdata.copy()
    rhb = rhb[(rhb['rightHandedBat'] == True)]
    if len(rhb) > 100:
        df2 = ((df1[(df1['bowler']== i)]))
        index = rhb.index
        balls = len(index)
        val_x = rhb['pitchX'].tolist()
        val_y = rhb['pitchY'].tolist()
        sdx = statistics.stdev(val_x)
        sdy = statistics.stdev(val_y)
        net_dev = math.sqrt(sdx*sdx + sdy*sdy)
        style = rhb['bowlingStyle'].tolist()
        df4 = pd.DataFrame({"Bowler":[i],"Balls Bowled": [balls], "batter_type":"RHB", "sdx":[sdx], "sdy":[sdy], "net_dev":[net_dev], "bowler_style":[style[0]]})
        result = result.append(df4)
    lhb = newdata.copy()
    lhb = lhb[(lhb['rightHandedBat'] == False)]
    if len(lhb) > 100:
        df3 = ((df1[(df1['bowler']== i)]))
        index = lhb.index
        balls = len(index)
        val_x = lhb['pitchX'].tolist()
        val_y = lhb['pitchY'].tolist()
        sdx = statistics.stdev(val_x)
        sdy = statistics.stdev(val_y)
        net_dev = math.sqrt(sdx*sdx + sdy*sdy)
        style = lhb['bowlingStyle'].tolist()
        df4 = pd.DataFrame({"Bowler":[i], "Balls Bowled": [balls], "batter_type":"LHB", "sdx":[sdx], "sdy":[sdy], "net_dev":[net_dev], "bowler_style":[style[0]]})
        result = result.append(df4)
        print(result)
result.to_csv(r'C:\Users\ninad\Desktop\Cricket Data\Bowlers Deviation.csv', index = False)