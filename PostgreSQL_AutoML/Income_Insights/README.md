# AutoML Leaderboard

| Best model   | name                    | model_type     | metric_type   |   metric_value |   train_time | Link                                              |
|:-------------|:------------------------|:---------------|:--------------|---------------:|-------------:|:--------------------------------------------------|
|              | 1_Baseline              | Baseline       | logloss       |       0.55108  |         0.39 | [Results link](1_Baseline/README.md)              |
|              | 2_DecisionTree          | Decision Tree  | logloss       |       0.369524 |        24.01 | [Results link](2_DecisionTree/README.md)          |
|              | 3_Linear                | Linear         | logloss       |       0.325353 |        14.45 | [Results link](3_Linear/README.md)                |
|              | 4_Default_RandomForest  | Random Forest  | logloss       |       0.323912 |        25.48 | [Results link](4_Default_RandomForest/README.md)  |
| **the best** | 5_Default_Xgboost       | Xgboost        | logloss       |       0.281087 |        31.77 | [Results link](5_Default_Xgboost/README.md)       |
|              | 6_Default_NeuralNetwork | Neural Network | logloss       |       0.316772 |        47.54 | [Results link](6_Default_NeuralNetwork/README.md) |
|              | Ensemble                | Ensemble       | logloss       |       0.281087 |         2.88 | [Results link](Ensemble/README.md)                |

### AutoML Performance
![AutoML Performance](ldb_performance.png)

### AutoML Performance Boxplot
![AutoML Performance Boxplot](ldb_performance_boxplot.png)