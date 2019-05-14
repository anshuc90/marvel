
# Marvel Data exploration with graphs


## Insights

1. Percentage Distribution of Top 10 Races: In the given data, the major chunk of races are unknown (47.28%). From the known races, Humans are the most common race (32.35%) followed by Mutants and Gods/Eternal

2. Percentage Distribution of Top 10 Publishers: Based on the given data, we can see that the market is dominated by the top 2 players- Marvel comics dominate the market by 56.23% forllowed by DC comics at 31.16%.

For the graphs below (3-8),
- gender is of 3 types- female, male and unknown 
- alignment is of 3 types- good, bad and neutral
- the unknown gender has 2 alignments only- good and bad

3. Intelligence distibution across Gender & Alignment: Percentage of intelligence is highest (62%) in neutral males and lowest for the unknown gender (25.6%).

4. Strength distibution across Gender & Alignment: Percentage of strength is highest (62%) in neutral males and lowest in neutral females (10%).

5. Speed distibution across Gender & Alignment: Percentage of speed is highest (48.5%) in neutral males and lowest for the unknown gender with good alignment (17%).

6. Durability distribution across Gender & Alignment: Percentage of durability is highest (76.1%) in neutral males followed by neutral females (70%) and lowest for the unknown gender with good alignment (24.7%).

7. Power distribution across Gender & Alignment: Percentage of power is highest (62%) in neutral females followed by neutral males (58.5%) and lowest for the unknown gender with good alignment (16.8%).

8. Combat distribution across Gender & Alignment: Percentage of combat is highest (70.4%) in neutral males and lowest for the unknown gender with bad alignment (11.8%).

9. Top 10 powerful charaters based on Total Stats: The top 10 powerful character have almost similar total stats (aggregation of all their traits). The most powerful comic character is Martian Manhunter.

10. Top 10 most powerful good charaters based on Total Stats: Using subset of data with only characters that have good alignment, we found that the most powerful good comic character is Martian Manhunter.

11. Top 10 most powerful bad charaters based on Total Stats: Using subset of data with only characters that have bad alignment, we found that the most powerful bad comic characters are Superboy Prime and General Zod.

12. Top 10 most appeared charaters based on frequency from 2008-2018: Using subset of data from 2008 to 2018, we found out that X-men as characters have appeared most in comics (15.32%) followed by Spider-Man (14.91%) followed by Iron Man (11.86%)


## Dependencies

### For DataFrame operations

import pandas as pd
import numpy as np

### For regular expression to treat special characters

import re

### For graphs

import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

Developed multiple graphs to gain an insight on the data provided:

## Datasets

characters.csv
charactersToComics.csv
superheroes_power_matrix.csv
charcters_stats.csv
comics.csv
marvel_characters_info.csv

I have made the code modular by incoporating functions.

## Types of graphs

1. Developed function to find percentage distribution of top 10 categorical variables (1 categorical variable per graph)

2. Developed function to show percentage distribution of each trait based on gender and alignment (3 categorical variables per graph)

3. Developed function to find percentage distribution of top 10 categorical variables on the basis of a continuous variable (1 categorical variable and 1 continuous variable per graph)

4. Developed function to plot a stacked graph on the basis of multiple categorical variables. For e.g. trait distribution amongst genders

In order to get deeper insights from the data, I have incorporated the above functions after preprocessing the data. Data preparation steps incorporated are listed below:

1. Filter data to work on subsets of data

2. Transform variables to create new features (E.g. RegEx, groupBy and transform)

3. Transform common variables by removing special characters in order to use them as join variables when merging datasets

4. Conversion of data types

5. Removal of duplicate rows from data