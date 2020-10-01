import pandas as pd
import numpy as np
import seaborn as sns

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
matches_data = pd.read_csv("./data/match.csv")
player_time_data = pd.read_csv('./data/player_time.csv')
players_data = players_data.merge(matches_data[["radiant_win", "match_id", "game_mode", 'duration']], on="match_id")



leavers_data = players_data[players_data.leaver_status get_ipython().getoutput("= 0]")
match_ids_having_left = leavers_data.match_id.unique()
left_mask = players_data['match_id'].isin(match_ids_having_left)
players_data = players_data[left_mask == False]
players_data


df = players_data[['hero_id', 'match_id', 'player_slot', 'radiant_win', 'leaver_status']]

heroes_number = df.hero_id.max()
rad_games = df[df['player_slot'] == 0][['match_id', 'hero_id']]
dir_games = df[df['player_slot'] == 1][['match_id', 'hero_id']]

# clean those who have left
# rad_games = rad_games[rad_games.leaver_status == 0]
# dir_games = dir_games[dir_games.leaver_status == 0]

rad_heroes = pd.pivot_table(rad_games, index='match_id', aggfunc=len, columns='hero_id', fill_value=0)

dir_heroes = pd.pivot_table(dir_games, index='match_id', aggfunc=len, columns='hero_id', fill_value=0)
dir_heroes.columns += heroes_number + 1

features_df = rad_heroes.merge(dir_heroes, on='match_id')

responses = df.drop_duplicates(subset='match_id', keep="last")['radiant_win']


def predict(vector):
    rad_prob = lr.predict(X_test.iloc[:, np.r_[:113, 111:220]])


X_train, X_test, y_train, y_test = train_test_split(features_df.iloc[:, np.r_[:113, 111:220]], responses,
                                                    test_size=0.10, random_state=44)
lr = LogisticRegression()
clf = lr.fit(X_train, y_train)
clf.score(X_test, y_test)



indices = np.r_[:113, 111:220]
reversed_indices = np.r_[111:220, :113]

reversed_indices
rad_probs = clf.predict_proba(X_test.iloc[:, indices])[:, 1]
dir_probs = clf.predict_proba(X_test.iloc[:, reversed_indices])[:, 1]
ove_probs = (rad_probs + (dir_probs)) / 2
is_winning = ove_probs > 0.5
# # # is_winning
sum(is_winning == y_test) / y_test.shape[0]
# # X_test2


get_ipython().run_cell_magic("html", "", """<style>
table {float:left}
</style>""")



