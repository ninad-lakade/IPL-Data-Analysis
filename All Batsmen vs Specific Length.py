import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_rows", None, "display.max_columns", None)
pd.set_option('display.width', 1000)
data = pd.read_csv(r'C:\Cricket Adda\T20 Data\IPL Ball Tracking Data\ipl_matches.csv')
df = pd.DataFrame(data, columns = ['batter_name', 'batter', 'bowler_name', 'bowl_style', 'length_type', 'year', 'match_id', 'match_inn', 'over_ball', 'over_num', 'speed', 'player_dismissed', 'total_extras', 'runs', 'bowler_extras', 'otw', 'length', 'bowler_style'])
final = pd.DataFrame(columns = ['Batsman', 'Length', 'Runs', 'Balls', 'Outs', 'Average', 'SR', 'BPB', 'DBP'])
df = df[df['year'] >= 2018]
#df = df[df['speed'] > 140]
df = df[df['over_num'] < 21]
#df = df[df['bowler_style'] == 'Pace']
ball = 'Yorker'
for i in df['batter_name'].unique():
    new_df = df[df['batter_name'] == i]
    df1 = new_df[new_df['length_type'] == 'Full toss']
    index = df1.index
    balls_ft = len(index)
    runs_ft = df1['runs'].sum()
    outs = df1[df1['player_dismissed'] == df1['batter']]
    index = outs.index
    outs_ft = len(index)
    boundaries = (df1[(df1['runs'] == 4) | (df1['runs'] == 6)])
    index = boundaries.index
    boundaries_ft = len(index)
    dots = df1[df1['runs'] == 0]
    index = dots.index
    dots_ft = len(index)
    if boundaries_ft>0:
        bpb_ft = round(balls_ft/boundaries_ft,2)
    else:
        bpb_ft = 0
    if balls_ft > 0:
        dpb_ft = round((dots_ft/balls_ft)*100,2)
    else:
        dpb_ft = 0
    avg_ft = round(runs_ft/outs_ft,2)
    sr_ft = round((runs_ft/balls_ft)*100,2)
    df2 = new_df[new_df['length_type'] == 'Yorker']
    index = df2.index
    balls_y = len(index)
    runs_y = df2['runs'].sum()
    outs = df2[df2['player_dismissed'] == df2['batter']]
    index = outs.index
    outs_y = len(index)
    boundaries = (df2[(df2['runs'] == 4) | (df2['runs'] == 6)])
    index = boundaries.index
    boundaries_y = len(index)
    dots = df2[df2['runs'] == 0]
    index = dots.index
    dots_y = len(index)
    if boundaries_y > 0:
        bpb_y = round(balls_y/boundaries_y,2)
    else:
        bpb_y = 0
    if balls_y > 0:
        dpb_y = round((dots_y/balls_y)*100,2)
    else:
        dpb_y = 0
    avg_y = round(runs_y/outs_y,2)
    sr_y = round((runs_y/balls_y)*100,2)
    df3 = new_df[new_df['length_type'] == 'Full']
    index = df3.index
    balls_f = len(index)
    runs_f = df3['runs'].sum()
    outs = df3[df3['player_dismissed'] == df3['batter']]
    index = outs.index
    outs_f = len(index)
    boundaries = (df3[(df3['runs'] == 4) | (df3['runs'] == 6)])
    index = boundaries.index
    boundaries_f = len(index)
    dots = df3[df3['runs'] == 0]
    index = dots.index
    dots_f = len(index)
    if boundaries_f > 0:
        bpb_f = round(balls_f/boundaries_f,2)
    else:
        bpb_f = 0
    if balls_f > 0:
        dpb_f = round((dots_f/balls_f)*100,2)
    else:
        dpb_f = 0
    avg_f = round(runs_f/outs_f,2)
    sr_f = round((runs_f/balls_f)*100,2)
    df4 = new_df[new_df['length_type'] == 'Good']
    index = df4.index
    balls_g = len(index)
    runs_g = df4['runs'].sum()
    outs = df4[df4['player_dismissed'] == df4['batter']]
    index = outs.index
    outs_g = len(index)
    boundaries = (df4[(df4['runs'] == 4) | (df4['runs'] == 6)])
    index = boundaries.index
    boundaries_g = len(index)
    dots = df4[df4['runs'] == 0]
    index = dots.index
    dots_g = len(index)
    if boundaries_g > 0:
        bpb_g = round(balls_g/boundaries_g,2)
    else:
        bpb_g = 0
    if balls_g > 0:
        dpb_g = round((dots_g/balls_g)*100,2)
    else:
        dpb_g = 0
    avg_g = round(runs_g/outs_g,2)
    sr_g = round((runs_g/balls_g)*100,2)
    df5 = new_df[new_df['length_type'] == 'Short']
    index = df5.index
    balls_s = len(index)
    runs_s = df5['runs'].sum()
    outs = df5[df5['player_dismissed'] == df5['batter']]
    index = outs.index
    outs_s = len(index)
    boundaries = (df5[(df5['runs'] == 4) | (df5['runs'] == 6)])
    index = boundaries.index
    boundaries_s = len(index)
    dots = df5[df5['runs'] == 0]
    index = dots.index
    dots_s = len(index)
    if boundaries_s > 0:
        bpb_s = round(balls_s/boundaries_s,2)
    else:
        bpb_s = 0
    if balls_s > 0:
        dpb_s = round((dots_s/balls_s)*100,2)
    else:
        dpb_s = 0
    avg_s = round(runs_s/outs_s,2)
    sr_s = round((runs_s/balls_s)*100,2)
    result = pd.DataFrame({'Batsman':[i, i, i, i, i], 'Length':['Full toss', 'Yorker', 'Full', 'Good', 'Short'], 'Runs':[runs_ft, runs_y, runs_f, runs_g, runs_s], 'Balls':[balls_ft, balls_y, balls_f, balls_g, balls_s], 'Outs':[outs_ft, outs_y, outs_f, outs_g, outs_s], 'Average':[avg_ft, avg_y, avg_f, avg_g, avg_s], 'SR':[sr_ft, sr_y, sr_f, sr_g, sr_s], 'BPB':[bpb_ft, bpb_y, bpb_f, bpb_g, bpb_s], 'DBP':[dpb_ft, dpb_y, dpb_f, dpb_g, dpb_s]})
    final = final.append(result)
final = final[final['Length'] == ball]
final = final[final['Balls'] > 0]
final.sort_values(by=['SR'], inplace=True, ascending=False)
print(final)
