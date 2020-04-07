RAPIDAPIKEY = '3f3da49864msh406c749262adb4ap11d6ecjsnffd6f68972fc'
import http.client
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
conn = http.client.HTTPSConnection("api-football-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': RAPIDAPIKEY
    }
conn.request("GET", "/v2/leagueTable/524", headers=headers)
##################################################################################################################
resp  = conn.getresponse()
data = resp.read().decode("utf-8")

print(type(data))
print(data)
persons = json.loads(data)
##################################################################################################################
persons.keys()
print(persons)
##################################################################################################################
team = []
homewin = []
awaywin = []
homeloss=[]
awayloss = []
totalplayed=[]
goalsDiff = []

for i in range(20):
    team.append(persons['api']['standings'][0][i]['teamName'])
    totalplayed.append(persons['api']['standings'][0][i]['all']['matchsPlayed'])
    homewin.append(persons['api']['standings'][0][i]['home']['win'])
    awaywin.append(persons['api']['standings'][0][i]['away']['win'])
    homeloss.append(persons['api']['standings'][0][i]['home']['lose'])
    awayloss.append(persons['api']['standings'][0][i]['away']['lose'])
    goalsDiff.append(persons['api']['standings'][0][i]['goalsDiff'])
    
###############################################################################################
stats_df_BAD = pd.DataFrame(persons['api']['standings'][0])
stats_df_BAD
##############################################################################################
#Liverpools Dominance
#homewin awaywin homeloss awayloss
width = 0.35       # the width of the bars

N=20
ind = np.arange(N)
fig = plt.figure()
ax = fig.add_subplot(111)
rects1 = ax.bar(ind, homewin, width, color='royalblue')

rects2 = ax.bar(ind+width, awaywin, width, color='seagreen')

# add some
ax.set_ylabel('Wins')
ax.set_title('Home and away wins by teams')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(team, rotation=90)

ax.legend( (rects1[0], rects2[0]), ('Home', 'Away') )
def autolabel(rects):
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
######################################################################################
#Liverpools Dominance
width = 0.35       # the width of the bars

N=20
ind = np.arange(N)
fig = plt.figure()
ax = fig.add_subplot(111)

rects1 = ax.bar(ind, homeloss, width, color='royalblue')

rects2 = ax.bar(ind+width, awayloss, width, color='seagreen')

# add some

ax.set_ylabel('Loss')
ax.set_title('Home and away loss by teams')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(team, rotation=90)

ax.legend( (rects1[0], rects2[0]), ('Home', 'Away') )
def autolabel(rects):
    
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                '%d' % int(height),
                ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)

plt.show()
########################################################################################
# Liverpools Dominance
z = []
for i in range(20):
        z.append(persons['api']['standings'][0][i]['points'])

ymin = min(z)

ymax = max(z)

plt.title("Team Distribution")
plt.ylabel('Count')
plt.xlabel('Points')
bi = [20,30,40,50,60,70,80,90]
counts, bins,_= plt.hist(z,bins =bi,rwidth =0.80, range = (ymin,ymax),color = 'orange',edgecolor = 'black',align="left")
plt.xticks(bins)
for n, b in zip(counts, bins):
        plt.gca().text(b-1, n+0.05, int(n));
plt.show()
#########################################################################################################
Points=[]
for i in range(20):
    Points.append(persons['api']['standings'][0][i]['points'])
#Liverpools Dominance
fig1, ax1 = plt.subplots(figsize=(30,10))
explode = (0.25, 0.2, 0.15, 0.1,0.05,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
ax1.pie(Points,labels = team,shadow = False,startangle = 0,autopct='%1.1f%%',explode = explode)
ax1.set(Title = "Total points Comparison")
plt.tight_layout()
plt.show()
###########################################################################################################
# Tight Run for the last Champions league spot
x = []
y = []
for i in range(20):
    if(4 <=  persons['api']['standings'][0][i]['rank'] <= 10):
        x.append(persons['api']['standings'][0][i]['teamName'])
        y.append(persons['api']['standings'][0][i]['points'])
fig1, ax1 = plt.subplots(figsize=(10,5))
ax1.set(Title = 'Point Comparison of 4th spot to 10th spot',xlabel = "Teams",ylabel = "Points")

ax1.bar(x,y,color = ['blue','red','yellow','magenta','cyan','green','black'])

plt.tight_layout()
plt.show()
###########################################################################################################
#Relegation Battle
rel_teams = []
rel_points = []
for i in range(20):
    if(persons['api']['standings'][0][i]['points']<35):
        rel_teams.append(persons['api']['standings'][0][i]['teamName'])
        rel_points.append(persons['api']['standings'][0][i]['points'])
fig, ax = plt.subplots()    
ax.barh(rel_teams,rel_points)

for i, v in enumerate(rel_points):
    ax.text(v + 0.1, i + 0, str(v), color='blue', fontweight='bold')
ax.set(Title = "Relegation Battle",xlabel = "Points",ylabel = "Teams");
plt.show()
###############################################################################################################