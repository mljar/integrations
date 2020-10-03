# AutoML Leaderboard

| Best model   | name                    | model_type     | metric_type   |   metric_value |   train_time | Link                                              |
|:-------------|:------------------------|:---------------|:--------------|---------------:|-------------:|:--------------------------------------------------|
|              | 1_Baseline              | Baseline       | logloss       |      0.242292  |         0.2  | [Results link](1_Baseline/README.md)              |
|              | 2_DecisionTree          | Decision Tree  | logloss       |      0.0597818 |        18.63 | [Results link](2_DecisionTree/README.md)          |
|              | 3_Linear                | Linear         | logloss       |      0.048105  |         6.09 | [Results link](3_Linear/README.md)                |
|              | 4_Default_RandomForest  | Random Forest  | logloss       |      0.0533721 |        14.51 | [Results link](4_Default_RandomForest/README.md)  |
|              | 5_Default_Xgboost       | Xgboost        | logloss       |      0.0469187 |         6.9  | [Results link](5_Default_Xgboost/README.md)       |
|              | 6_Default_NeuralNetwork | Neural Network | logloss       |      0.0537367 |        12.71 | [Results link](6_Default_NeuralNetwork/README.md) |
| **the best** | Ensemble                | Ensemble       | logloss       |      0.0446415 |         0.87 | [Results link](Ensemble/README.md)                |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)