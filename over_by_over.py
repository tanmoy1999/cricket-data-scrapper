#

# https://hs-consumer-api.espncricinfo.com/v1/pages/match/balls/wagon?lang=en&filterMatchId=1388407
# https://hs-consumer-api.espncricinfo.com/v1/pages/match/balls/wagon?lang=en&filterMatchId=1388407 ball by ball

import requests
import json
import pandas as pd


url = 'https://hs-consumer-api.espncricinfo.com/v1/pages/match/overs/details?lang=en&seriesId=1388374&matchId=1388407&mode=ALL'
df = pd.DataFrame(columns=["inningNumber","overNumber", "overRuns", "overWickets", "isComplete", "totalBalls", "totalRuns", "totalWickets","bowlersId","bowlersName", "requiredRunRate", "remainingBalls"])


response = requests.get(url)


if response.status_code == 200:
    data = response.json()
    # print(data['inningOvers'][0]['stats'][0]['bowlers'])

    for i in range(len(data['inningOvers'])):
      inningNumber = i
      for j in range(len(data['inningOvers'][i]['stats'])):
        overNumber = data['inningOvers'][i]['stats'][j]['overNumber']
        overRuns = data['inningOvers'][i]['stats'][j]['overRuns']
        overWickets = data['inningOvers'][i]['stats'][j]['overWickets']
        isComplete = data['inningOvers'][i]['stats'][j]['isComplete']
        totalBalls = data['inningOvers'][i]['stats'][j]['totalBalls']
        totalRuns = data['inningOvers'][i]['stats'][j]['totalRuns']
        totalWickets = data['inningOvers'][i]['stats'][j]['totalWickets']
        bowlersId = data['inningOvers'][i]['stats'][j]['bowlers'][0]['id']
        bowlersName = data['inningOvers'][i]['stats'][j]['bowlers'][0]['longName']
        requiredRunRate = data['inningOvers'][i]['stats'][j]['requiredRunRate']
        remainingBalls = data['inningOvers'][i]['stats'][j]['remainingBalls']
        balls_uid = data['inningOvers'][i]['stats'][j]['totalWickets']
        totalWickets = data['inningOvers'][i]['stats'][j]['totalWickets']
        df1 = pd.DataFrame(data=[[inningNumber,overNumber, overRuns, overWickets, isComplete, totalBalls, totalRuns, totalWickets,bowlersId,bowlersName, requiredRunRate, remainingBalls]],columns=["inningNumber","overNumber", "overRuns", "overWickets", "isComplete", "totalBalls", "totalRuns", "totalWickets","bowlersId","bowlersName", "requiredRunRate", "remainingBalls"])
        df = pd.concat([df,df1], axis=0)
df.to_csv('over_by_over.csv',index=False)
