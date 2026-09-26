# importing libraries
import pandas as pd

# reading the csv file
df = pd.read_csv('/data/games.csv')

# creating a sample of 50 rows from the dataframe and saving it to a new csv file
df.sample(50).to_csv('data/sample_games.csv', index=False)