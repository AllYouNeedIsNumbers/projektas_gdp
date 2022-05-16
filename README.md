# GDP per capita prediction
## Project overview and objective
Using World Economic Outlook Database data create a model that would predict a country’s GDP per capita from 5 main metrics

## Data, metrics, model results and model selection
###Data:
* European Union countries (EU)
* NATO countries (NATO)
###Metrics:
* General government revenue | Percent of GDP
* General government total expenditure | National currency | Billions
* Gross national savings | Percent of GDP
* Total investment | Percent of GDP
* Unemployment rate | Percent of total labor force
###Model results:
* EU countries results without outliers:

|Model                      | MSE      | MAPE  |
|:--------------------------|:--------:| -----:|
| XGBoost with GridSearchCV | 6445.466 | 0.302 |
| XGBoost                   | 5145.220 | 0.209 |
| Linear Regression         | 10102.123| 0.515 |

* NATO countries results without outliers:

|Model                      | MSE      | MAPE  |
|:--------------------------|:--------:| -----:|
|**XGBoost with GridSearchCV**|**5093.802**|**0.171**|
| XGBoost                   | 5435.499 | 0.180 |
| Linear Regression         | 14311.165| 0.751 |


###Model selection:
Selected model: **XGBoost with GridSearchCV**

Selected dataset: **NATO countries results without outliers**

Final metrics: **MSE** 5093.802, **MAPE** 0.171

##Instructions to run the API server:
1. Clone the project from github
2. Run the 'requirements.txt' file to install libraries
3. Run the 'model.py'
4. Run 'app.py' 
5. Launch the API server link shown in the terminal and enter the values for indicated metrics

**To review the full project run "Project.ipynb"**

##Project comments, results and conclusions
* Completed a data analysis on the World Economic Outlook Database data containing 196 countries macroeconomic metrics. Data is available from 1980 to the present however there were many null values before the 2000s
so the model used data from 2000 until 2019. Also, for a more accurate  GDP per capita prediction the model used only NATO countries without Luxembourg (outlier in the model)
* The best performing model was **XGBoost model with NATO data** which was using 19 metrics to predict GDP per capita:
  * MSE: 3677.753
  * MAPE: 0.121 (this shows that the prediction was off by ~12%)
* The final selected model which was using only 5 metrics was **XGBoost with GridSearchCV using NATO data without outliers** and the results for it were:
  * MSE: 5093.802
  * MAPE: 0.171 (this shows that the prediction was off by ~17%)
* As seen from the results the final model was still able to perform well and have a relatively good MAPE (Mean Absolute Percentage Error)
* The model is intended to be used to predict NATO countries GDP per capita. Also, the model could be used to predict other countries GDP per capita however the results may not be as accurate as with NATO countries.