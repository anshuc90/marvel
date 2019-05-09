import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib import animation
import seaborn as sns



pd.set_option('display.max_columns', None)

# read data
characters = pd.read_csv("data/characters.csv")
char2comm = pd.read_csv("data/charactersToComics.csv")
superpower = pd.read_csv("data/superheroes_power_matrix.csv")
charStats = pd.read_csv("data/charcters_stats.csv")
comics = pd.read_csv("data/comics.csv")

#drop description column from comics data
comics = comics.drop(columns="description")

#merging datasets on common variables
merged1 = pd.merge(characters, char2comm, left_on='characterID', right_on='characterID', how="right")
merged2 = pd.merge(comics, merged1, left_on='comicID', right_on='comicID', how="right")

#making feature variables

#extracting (year) from title 
merged2['comicYear'] = merged2['title'].str.extract('(\d\d\d\d)', expand= True)

#separating charName from name
merged2[['characterName', 'origName']] = merged2['name'].str.split('(', expand= True)

#formatting join variables- origName and charName
merged2['origName'] = merged2['origName'].str.replace('[^\w]', '')
merged2['characterName'] = merged2['characterName'].str.replace('[^\w]', '')
charStats['Name'] = charStats['Name'].str.replace('[^\w]', '')
superpower['Name'] = superpower['Name'].str.replace('[^\w]', '')

#merging datasets on common variables
merged3 = pd.merge(charStats, merged2, left_on='Name', right_on='characterName', how="right")
merged4 = pd.merge(superpower, merged3, left_on='Name', right_on='characterName', how="right")

#drop columns
merged4.drop(["Name_x","Name_y","name"], axis=1, inplace=True)

#remove duplicates
merged5 = merged4[~merged4[['comicID','characterID']].apply(frozenset, axis=1).duplicated()]
print(merged5.head())

#merged5.to_csv("result/res2.csv")

