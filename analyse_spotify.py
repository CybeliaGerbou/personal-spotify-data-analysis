import pandas as pd
import glob

parent_folder = "/Users/utsuk/Documents/DATA SCIENCE/Analyse de données personnelles spotify/dataset/Spotify Account Data"

file_name = "StreamingHistory_music_0.json"

df = pd.DataFrame()

for file in glob.glob(parent_folder + '/' + file_name):
    temp = pd.read_json(file)
    df = pd.concat([df, temp])

# PREPROCESSING

