import pandas as pd
import numpy as np
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

sns.set(style="ticks", color_codes=True, font_scale=1.4)
sns.set_context("paper", rc={"font.size":10,"axes.titlesize":10,"axes.labelsize":10}) 
pd.set_option('display.max_columns', None)

# read data
characters = pd.read_csv("data/characters.csv")
char2comm = pd.read_csv("data/charactersToComics.csv")
superpower = pd.read_csv("data/superheroes_power_matrix.csv")
charStats = pd.read_csv("data/charcters_stats.csv")
comics = pd.read_csv("data/comics.csv")
marvelChar = pd.read_csv("data/marvel_characters_info.csv")


####################################################################################################################################
####################################################################################################################################

# 1. basic graph (1 col- top 10)

def basic_count_graph(df, col, title):
	ax = df[col].value_counts()[:10].plot(kind='bar', figsize=(8,8), fontsize=13)
	ax.set_alpha(0.9)
	ax.set_title(title, fontsize=16)
	ax.set_ylabel("Total Percentage ", fontsize=15)
	totals = []
	for i in ax.patches:
		totals.append(i.get_height())
	total = sum(totals)
	for i in ax.patches:
		ax.text(i.get_x()-.03, i.get_height()+.5, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=12,color='dimgrey')
	for i in ax.get_xticklabels():
		i.set_rotation(20)
	plt.show()

def draw_basic_counts():
	#a. top 10 races (frequency distribution)
	basic_count_graph(marvelChar, 'Race', 'Percentage Distribution of Top 10 Races',)

	#b. top 10 publishers (frequency distribution)
	basic_count_graph(marvelChar, 'Publisher', 'Percentage Distribution of Top 10 Publishers')

####################################################################################################################################
####################################################################################################################################

# 2. basic graph (3 col distribution graph)

def basic_bar_sns(df, col, col2, col3, title):
	plt.figure(figsize=(8, 8))
	ax = sns.barplot(x=col,y=col2,data=df, hue=col3, ci=None)
	ax.set_title(title, fontsize=16)
	ax.set_ylabel("Total Percentage ", fontsize=12)
	for p in ax.patches:
		ax.annotate(format(p.get_height(), '.2f')+'%', (p.get_x() + p.get_width() / 2., p.get_height()), ha = 'center', va = 'center', xytext = (0, 10), textcoords = 'offset points')
	plt.show()

# marvelChar and charStats

#remove all special characters
charStats['Name'] = charStats['Name'].str.replace('[^\w]', '')
marvelChar['Name'] = marvelChar['Name'].str.replace('[^\w]', '')

#merging datasets on common variables
merged_fin1 = pd.merge(charStats, marvelChar, left_on='Name', right_on='Name', how="right")
#print(merged_fin1.dtypes)

def draw_basic_bars():
	basic_bar_sns(merged_fin1, 'Gender', 'Intelligence', 'Alignment_x', 'Intelligence distibution across Gender & Alignment')
	basic_bar_sns(merged_fin1, 'Gender', 'Strength', 'Alignment_x', 'Strength distibution across Gender & Alignment')
	basic_bar_sns(merged_fin1, 'Gender', 'Speed', 'Alignment_x', 'Speed distibution across Gender & Alignment')
	basic_bar_sns(merged_fin1, 'Gender', 'Durability', 'Alignment_x', 'Durability distibution across Gender & Alignment')
	basic_bar_sns(merged_fin1, 'Gender', 'Power', 'Alignment_x', 'Power distibution across Gender & Alignment')
	basic_bar_sns(merged_fin1, 'Gender', 'Combat', 'Alignment_x', 'Combat distibution across Gender & Alignment')

####################################################################################################################################
####################################################################################################################################


#data preprocessing

#comics and characters 

#drop description column from comics data
comics = comics.drop(columns="description")

#extracting (year) from title
comics['comicYear'] = comics['title'].str.extract('(\d\d\d\d)', expand= True)
comics['comicYear'] = pd.to_numeric(comics['comicYear'])

#separating charName from name and stripping blanks
characters[['characterName', 'origName']] = characters['name'].str.split('(', expand= True)
characters['characterName'] = characters['characterName'].str.strip()

#merging datasets on common variables
merged1 = pd.merge(characters, char2comm, left_on='characterID', right_on='characterID', how="right")
merged2 = pd.merge(comics, merged1, left_on='comicID', right_on='comicID', how="right")

#remove duplicates
merged_fin2 = merged2[~merged2[['comicID','characterID']].apply(frozenset, axis=1).duplicated()]

#take subset of data for last 10 years- 2008-2018
merged_fin2 = merged_fin2[(merged_fin2['comicYear'] >= 2008) & (merged_fin2['comicYear'] <= 2018)]

#count of freq of char as a new column 
merged_fin2['countChar'] = merged_fin2.groupby('characterName')['characterName'].transform(len)

#remove duplicates
merged_fin3 = merged_fin2[~merged_fin2[['characterName']].apply(frozenset, axis=1).duplicated()]


#3. basic graph (2 cols- top 10)

def basic_relation_graph(df, col, col2, title):
	ax = df.sort_values(by=[col], ascending=False)[:10].plot(kind='bar', figsize=(8,8), x=col2, y=col)
	ax.set_alpha(0.9)
	ax.set_title(title, fontsize=16)
	ax.set_ylabel("Total Percentage ", fontsize=12)
	totals = []
	for i in ax.patches:
		totals.append(i.get_height())
	total = sum(totals)
	for i in ax.patches:
		ax.text(i.get_x()-.03, i.get_height()+.5, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=12,color='dimgrey')
	for i in ax.get_xticklabels():
		i.set_rotation(20)
	plt.show()

def draw_basic_relations():

	#a. basic -top 10 powerful charaters(char names) based on total(stats) column
	basic_relation_graph(charStats, 'Total', 'Name', 'Top 10 powerful charaters based on Total Stats')

	#b. basic -top 10 powerful good & bad characters based on total stats

	#take subset of data - only include good -alignment
	charStats_good = charStats[(charStats['Alignment'] == 'good')]

	basic_relation_graph(charStats_good, 'Total', 'Name', 'Top 10 most powerful good charaters based on Total Stats')

	#take subset of data - only include bad -alignment
	charStats_bad = charStats[(charStats['Alignment'] == 'bad')]

	basic_relation_graph(charStats_bad, 'Total', 'Name', 'Top 10 most powerful bad charaters based on Total Stats')

	#c. basic -top 10 count of characters in last 10 years

	basic_relation_graph(merged_fin3, 'countChar', 'characterName', 'Top 10 most appeared charaters based on frequency from 2008-2018')


####################################################################################################################################
####################################################################################################################################


# 3. basic stack graph (1 x-axis col, multiple y-axis cols)

def basic_stack_graph(df, col, col2, title, ticks):
	ax = df.groupby(col).nunique().plot(kind="bar",  figsize=(8,8), stacked=True, x=col, y= col2)
	ax.set_alpha(0.9)
	ax.set_title(title, fontsize=16)
	ax.set_ylabel("Total Percentage ", fontsize=12)
	totals = []
	for i in ax.patches:
		totals.append(i.get_height())
	total = sum(totals)
	for i in ax.patches:
		ax.text(i.get_x()-.03, i.get_height()+.5, \
            str(round((i.get_height()/total)*100, 2))+'%', fontsize=15,color='dimgrey')
	ax = plt.gca()
	ax.set_xticks([0,1,2])
	ax.set_xticklabels(ticks)
	plt.show()

def draw_basic_stack():
	#a. trait distribution within Alignment distribution (frequency)
	basic_stack_graph(charStats, 'Alignment', ['Intelligence','Strength','Speed','Durability','Power','Combat'], 'Trait distribution based on Alignment', ['good','bad', 'neutral'])

	#b. trait distribution within gender distribution (frequency)
	basic_stack_graph(merged_fin1, 'Gender', ['Intelligence','Strength','Speed','Durability','Power','Combat'], 'Trait distribution based on Gender', ['male','female', '-'])


####################################################################################################################################
####################################################################################################################################

#.set_index(col) .reset_index(name=col)
#np.arange(len(df[col].drop_duplicates()))
#.apply(lambda x: x.reset_index(drop=True)).drop('A',axis=1).reset_index()

#merged_fin2.to_csv('result/res2.csv')

if __name__ == "__main__":
	draw_basic_stack()



