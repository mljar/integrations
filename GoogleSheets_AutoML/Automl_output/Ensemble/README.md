# Summary of Ensemble

## Ensemble structure
| Model          |   Weight |
|:---------------|---------:|
| 2_DecisionTree |        1 |

## Metric details
|           |    score |    threshold |
|:----------|---------:|-------------:|
| logloss   | 0.06295  | nan          |
| auc       | 0.935354 | nan          |
| f1        | 0.914286 |   0.010491   |
| accuracy  | 0.989324 |   0.010491   |
| precision | 0.96     |   0.010491   |
| recall    | 1        |   0.00944188 |
| mcc       | 0.90978  |   0.010491   |


## Confusion matrix (at threshold=0.010491)
|                     |   Predicted as negative |   Predicted as positive |
|:--------------------|------------------------:|------------------------:|
| Labeled as negative |                    1572 |                       4 |
| Labeled as positive |                      14 |                      96 |

## Learning curves
![Learning curves](learning_curves.png)