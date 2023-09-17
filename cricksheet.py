import os
import requests
import json
import pandas as pd
import zipfile

def zip_files():
  # Define the URL of the ZIP file you want to download
  zip_url = "https://cricsheet.org/downloads/ipl_json.zip"

  # Specify the folder where you want to save the downloaded ZIP file
  download_folder = "downloaded_files"
  os.makedirs(download_folder, exist_ok=True)

  # Download the ZIP file
  response = requests.get(zip_url)
  zip_file_path = os.path.join(download_folder, "ipl.zip")

  with open(zip_file_path, 'wb') as zip_file:
      zip_file.write(response.content)

  # Specify the folder where you want to unzip the contents
  unzip_folder = "unzipped_files"
  os.makedirs(unzip_folder, exist_ok=True)

  # Unzip the downloaded file to the specified folder
  with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
      zip_ref.extractall(unzip_folder)

  # Clean up: Remove the downloaded ZIP file if needed
  # os.remove(zip_file_path)

  print("Downloaded and unzipped successfully.")
def mem_used():
    memory_usage = df.memory_usage(deep=True).sum()
    memory_usage_mb = memory_usage / (1024 ** 2)
    print(f"Memory usage: {memory_usage_mb:.2f} MB")

def get_value(data, *keys, default=None):
    try:
        for key in keys:
            data = data[key]
        return data
    except (KeyError, TypeError):
        return default

if __name__ == "__main__":
  # zip_files("https://cricsheet.org/downloads/ipl_json.zip")
  df = pd.DataFrame(columns=["match_date","event_matchnum","event_name","gender","match_type","official_match_referees","winner","by_runs","by_wickets","overs","player_of_match","season","team_type","team_1","team_2","toss_winner","toss_decision","venue","innings","team","over","batter","bowler","non_striker","legbyes","runs","extras","total","filename"])

  # Specify the folder path
  folder_path = r"C:\Users\tanmo\Documents\cricket-data-scrapper\unzipped_files"

  filenames = os.listdir(folder_path)
  file_paths = [os.path.join(folder_path, filename) for filename in filenames]


  for file_path in file_paths:
      filename = file_path
      print(filename)
      mem_used()
      
      
      with open(file_path,'r') as json_file:
          data = json.load(json_file)

      
      match_date = get_value(data, 'info', 'dates', 0)
      event_matchnum = get_value(data, 'info', 'event', 'match_number')
      event_name = get_value(data, 'info', 'event', 'name')
      gender = get_value(data, 'info', 'gender')
      match_type = get_value(data, 'info', 'match_type')
      official_match_referees = str(get_value(data, 'info', 'officials'))
      winner = get_value(data, 'info', 'outcome', 'winner')
      by_runs = get_value(data, 'info', 'outcome', 'by', 'runs')
      by_wickets = get_value(data, 'info', 'outcome', 'by', 'wickets')
      overs = get_value(data, 'info', 'overs')
      player_of_match = get_value(data, 'info', 'player_of_match',0)
      season = get_value(data, 'info', 'season')
      team_type = get_value(data, 'info', 'team_type')
      team_1 = get_value(data, 'info', 'teams', 0)
      team_2 = get_value(data, 'info', 'teams', 1)
      toss_winner = get_value(data, 'info', 'toss', 'winner')
      toss_decision = get_value(data, 'info', 'toss', 'decision')
      venue = get_value(data, 'info', 'venue')

      for i in range(len(get_value(data, 'innings'))):
          innings = i
          team = get_value(data, 'innings', innings, 'team')
          for j in range(len(get_value(data, 'innings', innings, 'overs'))):
              over = get_value(data, 'innings', innings, 'overs', j, 'over')
              for ball in range(len(get_value(data, 'innings', innings, 'overs', j,'deliveries'))):
                  batter = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'batter')
                  bowler = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'bowler')
                  non_striker = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'non_striker')
                  legbyes = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'extras','legbyes')
                  runs = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'runs','batter')
                  extras = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'runs','extras')
                  total = get_value(data, 'innings', innings, 'overs', j,'deliveries',ball,'runs','total')
                  df2 = pd.DataFrame(data=[[match_date,event_matchnum,event_name,gender,match_type,official_match_referees,winner,by_runs,by_wickets,overs,player_of_match,season,team_type,team_1,team_2,toss_winner,toss_decision,venue,innings,team,over,batter,bowler,non_striker,legbyes,runs,extras,total,filename]],columns=["match_date","event_matchnum","event_name","gender","match_type","official_match_referees","winner","by_runs","by_wickets","overs","player_of_match","season","team_type","team_1","team_2","toss_winner","toss_decision","venue","innings","team","over","batter","bowler","non_striker","legbyes","runs","extras","total","filename"])
                  df = pd.concat([df,df2], axis=0)
  df.to_excel('ipl_data.xlsx')
  df.to_csv('ipl_data.csv')
  
else:
    print ("Executed when imported")
            

