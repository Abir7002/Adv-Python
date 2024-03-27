import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/Abir Das/Desktop/Python programing/Adv Python/IPL_Matches_2022.csv")
##x1 = np.array([x])


data['team1'].value_counts()
data['team2'].value_counts()
data['team1'].value_counts() + data['team2'].value_counts()
total_matches_played = data['team1'].value_counts().add(data['team2'].value_counts(), fill_value=0).astype(int)
total_won= data['match_winner'].value_counts()
win_percentage = ((total_won / total_matches_played) * 100).sort_values(ascending=False).astype(int)
team_performance = pd.DataFrame({
'Total Matches Played': total_matches_played,
'Total Matches Won': total_won,
'Win Percentage (%)': win_percentage
}).sort_values(by='Win Percentage (%)', ascending=False)

print(team_performance.to_string())
