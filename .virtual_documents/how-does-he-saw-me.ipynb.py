import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as plt
from matplotlib.pyplot import figure


import gc
from subprocess import check_output


from sklearn.preprocessing import MinMaxScaler, StandardScaler, FunctionTransformer
from sklearn.preprocessing import PolynomialFeatures

from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.dummy import DummyRegressor

from sklearn.utils import check_array
from sklearn.base import TransformerMixin, BaseEstimator
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder

# Model assement functionality
from sklearn.model_selection import LeaveOneOut, KFold, train_test_split, cross_val_score


players_data = pd.read_csv("./data/players.csv")
player_time_data = pd.read_csv('./data/player_time.csv')
matches_data = pd.read_csv("./data/match.csv")


# Convert the timestamp to date
matches_data['start_time'] = pd.to_datetime(matches_data['start_time'], unit='s')

# filter only games where no player left the game
players_data = players_data[players_data.leaver_status == 0]



# merge players_data with matches
df = pd.merge(players_data, matches_data, on='match_id')


players_data.account_id.value_counts()


players_schema = pd.read_json("./schemas/players.json")
columns_titles = ['key', 'type', 'description']
players_schema = players_schema.reindex(columns=columns_titles)
pd.options.display.max_colwidth = 100
players_schema[60:120]


a_match = player_time_data[player_time_data['match_id'] == 1]
# a_match.T


a_match.iloc[:, 1:].plot.line(x='times', figsize=(10, 10));


import datetime
timestamp = datetime.datetime.fromtimestamp(1446750112)
print(timestamp.strftime('get_ipython().run_line_magic("Y-%m-%d", " %H:%M:%S'))")



# sns.lineplot(data=df.sort_values(by='start_time')[:400], x='start_time', y='gold_per_min')



