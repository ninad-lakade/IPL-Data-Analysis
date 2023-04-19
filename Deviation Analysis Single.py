import pandas as pd
import warnings
import statistics
import math
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\mensTestHawkeyeStats.csv')
df = data[(data['matchId']>=7000) & (data['matchId']<33762)]
df1 = df[(df['bowler']=='Ravindra Jadeja')]
temp = df1[['pitchX', 'pitchY', 'rightHandedBat', 'bowlingStyle']]
newdata = temp.dropna()
#newdata.to_csv(r'C:\Users\ninad\Desktop\Cricket Data\FINDJADDU.csv', index = False)
val_x = newdata['pitchX'].tolist()
val_y = newdata['pitchY'].tolist()
sdx = statistics.stdev(val_x)
sdy = statistics.stdev(val_y)
net_dev = math.sqrt(sdx*sdx + sdy*sdy)
#print('9000 to 10000')
print(sdx)
print(sdy)
print(net_dev)
print('    ')