import numpy as np  # linear algebra
import pandas as pd # data process cvs file 
import os
for dirname, _, filenames in os.walk('input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# results writen to current dir are saved as output
import pandas as pd
import xgboost as xgb
from decimal import Decimal
from IPython.display import display
from pandas.plotting import scatter_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC

data = pd.read_csv("input/stats.csv")

scatter_matrix(data[['TeamPoints', 'FieldGoals', 'X3PointShots', 'FreeThrows', 'Steals', 'Blocks', 'Turnovers', 'TotalFouls', 'TotalRebounds']], figsize=(15,15))
