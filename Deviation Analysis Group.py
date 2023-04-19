import pandas as pd
import warnings
import statistics
import math
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Users\ninad\Desktop\Cricket Data\mensTestHawkeyeStats.csv')
#df = pd.DataFrame(data, columns = ['pitchX', 'pitchY'])

#print(newdata)



df = data[(data['matchId']>=7000)]
for i in df['bowler'].unique():
    df1 = df[(df['bowler']==i)]
    temp = df1[['pitchX','pitchY']]
    newdata = temp.dropna()
    if len(newdata) > 500:
        
        val_x = newdata['pitchX'].tolist()
        val_y = newdata['pitchY'].tolist()
        SDX = statistics.stdev(val_x)
        SDY = statistics.stdev(val_y)
        print(i)
        print(SDX)
        print(SDY)
        Net_Dev = math.sqrt(SDX*SDX + SDY*SDY)
        print(Net_Dev)
        print('      ')
