import requests
import json
import pandas as pd

seriesId = '1388374'
matchId = '1388412'

url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/overs/details?lang=en&seriesId=' + seriesId + '&matchId='+ matchId +'&mode=ALL'
url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/overs/details?lang=en&seriesId=1388374&matchId=1388414&mode=ALL'
print(url)

df_BB = pd.DataFrame(columns=["inningNumber","balls_id","overNumber","oversUnique","oversActual","ballNumber","totalRuns","batsmanRuns","isFour","isSix","isWicket","outPlayerId","dismissalType","byes","legbyes","wides","wagonX","wagonY","wagonZone","timestamp","batsmanPlayerId","bowlerPlayerId","totalInningRuns","totalInningWickets","batsmanStatText","bowlerStatText"])

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    for i in range(len(data['inningOvers'])):
      for j in range(len(data['inningOvers'][i]['stats'])):
          for k in range(len(data['inningOvers'][i]['stats'][j]['balls'])):
              try:
                  balls_id = data['inningOvers'][i]['stats'][j]['balls'][k]['id']
                  inningNumber = int(data['inningOvers'][i]['stats'][j]['balls'][k]['inningNumber']) - 1
                  oversUnique = data['inningOvers'][i]['stats'][j]['balls'][k]['oversUnique']
                  oversActual = data['inningOvers'][i]['stats'][j]['balls'][k]['oversActual']
                  overNumber = int(data['inningOvers'][i]['stats'][j]['balls'][k]['oversActual']) + 1
                  ballNumber = data['inningOvers'][i]['stats'][j]['balls'][k]['ballNumber']
                  totalRuns = data['inningOvers'][i]['stats'][j]['balls'][k]['totalRuns']
                  batsmanRuns = data['inningOvers'][i]['stats'][j]['balls'][k]['batsmanRuns']
                  isFour = data['inningOvers'][i]['stats'][j]['balls'][k]['isFour']
                  isSix = data['inningOvers'][i]['stats'][j]['balls'][k]['isSix']
                  isWicket = data['inningOvers'][i]['stats'][j]['balls'][k]['isWicket']
                  outPlayerId = data['inningOvers'][i]['stats'][j]['balls'][k]['outPlayerId']
                  dismissalType = data['inningOvers'][i]['stats'][j]['balls'][k]['dismissalType']
                  byes = data['inningOvers'][i]['stats'][j]['balls'][k]['byes']
                  legbyes = data['inningOvers'][i]['stats'][j]['balls'][k]['legbyes']
                  wides = data['inningOvers'][i]['stats'][j]['balls'][k]['wides']
                  wagonX = data['inningOvers'][i]['stats'][j]['balls'][k]['wagonX']
                  wagonY = data['inningOvers'][i]['stats'][j]['balls'][k]['wagonY']            
                  wagonZone = data['inningOvers'][i]['stats'][j]['balls'][k]['wagonZone']            
                  timestamp = data['inningOvers'][i]['stats'][j]['balls'][k]['timestamp']            
                  batsmanPlayerId = data['inningOvers'][i]['stats'][j]['balls'][k]['batsmanPlayerId']            
                  bowlerPlayerId = data['inningOvers'][i]['stats'][j]['balls'][k]['bowlerPlayerId']
                  totalInningRuns = data['inningOvers'][i]['stats'][j]['balls'][k]['totalInningRuns']                        
                  totalInningWickets = data['inningOvers'][i]['stats'][j]['balls'][k]['totalInningWickets']                        
                  batsmanStatText = data['inningOvers'][i]['stats'][j]['balls'][k]['batsmanStatText']['long']                        
                  bowlerStatText = data['inningOvers'][i]['stats'][j]['balls'][k]['bowlerStatText']['long']
                  df2 = pd.DataFrame(data=[[inningNumber,balls_id,overNumber,oversUnique,oversActual,ballNumber,totalRuns,batsmanRuns,isFour,isSix,isWicket,outPlayerId,dismissalType,byes,legbyes,wides,wagonX,wagonY,wagonZone,timestamp,batsmanPlayerId,bowlerPlayerId,totalInningRuns,totalInningWickets,batsmanStatText,bowlerStatText]],columns=["inningNumber","balls_id","overNumber","oversUnique","oversActual","ballNumber","totalRuns","batsmanRuns","isFour","isSix","isWicket","outPlayerId","dismissalType","byes","legbyes","wides","wagonX","wagonY","wagonZone","timestamp","batsmanPlayerId","bowlerPlayerId","totalInningRuns","totalInningWickets","batsmanStatText","bowlerStatText"])
                  df_BB = pd.concat([df_BB,df2], axis=0)
              except:
                  print(i,j,k)
                  pass
df_BB.to_csv('ball_by_ball_indvsl_final.csv',index=False)

# Dismisal type 1 --> catch 2--> wicket 3 --> LBW