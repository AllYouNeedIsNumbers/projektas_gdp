import xgboost as xgb
import pandas as pd
from sklearn.model_selection import GridSearchCV, train_test_split
import pickle

# Load data from csv
df = pd.read_csv('../data/df_nato_final.csv')
print(df.head())
print(df.columns)


# split data
dep_var = 'Gross domestic product per capita, current prices | U.S. dollars | Units'
X = df[['General government revenue | Percent of GDP',
       'General government total expenditure | National currency | Billions',
       'Gross national savings | Percent of GDP',
       'Total investment | Percent of GDP',
       'Unemployment rate | Percent of total labor force',
       'Gross domestic product per capita, current prices | U.S. dollars | Units']]
y = df[dep_var]
X_train, X_test = train_test_split(X, test_size=0.20, random_state=0)
y_train = X_train[dep_var]
X_train.drop(dep_var, axis=1, inplace=True)
y_test = X_test[dep_var]
X_test.drop(dep_var, axis=1, inplace=True)

# GDP prediction model
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)
parameters = {'objective': ['reg:squarederror'],
              'learning_rate': [0.05, 0.1, 0.2, 0.3],
              'max_depth': [6, 8, 10, 12, 14],
              'verbosity': [0],
              'n_estimators': [5, 10, 15, 20, 1000], # number of trees, 1000 for better results
              }
bst = xgb.XGBRegressor()
best = GridSearchCV(bst, parameters, n_jobs=5, scoring="neg_mean_absolute_error", verbose=2, refit=True)
xgb_grid_fit = best.fit(X_train, y_train)
best_params = xgb_grid_fit.best_params_
best_params['eval_metric'] = 'mape'
evals = [(dtest, 'test'), (dtrain, 'train')]
# TRAIN
xgb_grid = xgb.train(best_params, dtrain, 500, evals=evals)
# PREDICT
y_pred_xgb_grid = xgb_grid.predict(dtest)


# Make pickle file of our model
with open('../flask_app/model.pickle', 'wb') as handle:
    pickle.dump(xgb_grid, handle, protocol=pickle.HIGHEST_PROTOCOL)

if __name__ == '__main__':
        ...